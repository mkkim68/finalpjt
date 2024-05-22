<template>
  <div class="container">
    <h1>은행 찾기</h1>
    <div class="main">
      <div class="search-panel">
        <div class="form-group">
          <label for="city">지역</label>
          <input type="text" v-model="cityInput" placeholder="검색할 지역을 입력하세요." class="form-control">
          <!-- <input type="text" v-model="districtInput" placeholder="구를 입력하세요" class="form-control"> -->
        </div>
        <div class="form-group">
          <label for="bank">은행</label>
          <select v-model="selectedOption" class="form-select">
            <option value="모든 은행">모든 은행</option>
            <option v-for="bank in uniqueBanks" :key="bank" :value="bank">{{ bank }}</option>
          </select>
        </div>
        <button @click="search">검색하기</button>
      </div>
      <div class="map-container">
        <div id="map" class="map"></div>
      </div>
    </div>
    <div class="bank-list" v-if="filteredBanks.length">
      <h4>검색된 은행 리스트</h4>
      <table>
        <thead style="text-align: center;">
          <tr>
            <th class="first">번호</th>
            <th class="second">지점명</th>
            <th class="third">주소</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(bank, index) in filteredBanks" :key="bank.id">
            <td style="text-align: center;">{{ index + 1 }}</td>
            <td style="font-weight: ;">{{ bank.place_name }}</td>
            <td>{{ bank.road_address_name || bank.address_name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;

let map, geocoder;
const cityInput = ref('');
const districtInput = ref('');
const selectedOption = ref('모든 은행');
const banks = ref([]);
const filteredBanks = ref([]);
const uniqueBanks = ref([]);

onMounted(() => {
  const script = document.createElement('script');
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services,clusterer&autoload=false`;
  script.onload = () => {
    window.kakao.maps.load(() => {
      const container = document.getElementById('map');
      const options = {
        center: new window.kakao.maps.LatLng(37.5665, 126.9780), // 초기 위치 (서울)
        level: 3 // 초기 줌 레벨
      };
      map = new window.kakao.maps.Map(container, options);
      geocoder = new window.kakao.maps.services.Geocoder();
    });
  };
  document.head.appendChild(script);
});

watch(banks, (newBanks) => {
  const bankNames = newBanks.map(bank => bank.place_name.split(' ')[0]);
  uniqueBanks.value = [...new Set(bankNames)];
});

const search = () => {
  const fullAddress = `${cityInput.value} ${districtInput.value}`;
  geocoder.addressSearch(fullAddress, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
      map.setCenter(coords);
      searchBanks(coords);
    } else {
      console.error('주소 검색 실패:', status);
    }
  });
};

const searchBanks = (coords) => {
  const places = new window.kakao.maps.services.Places();
  const callback = (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      banks.value = result; // 모든 검색 결과 저장
      filterBanks(); // 필터 적용
    } else {
      console.error('은행 검색 실패:', status);
    }
  };

  places.categorySearch('BK9', callback, {
    location: coords,
    radius: 1000 // 검색 반경 (미터)
  });
};

const filterBanks = () => {
  clearMarkers(); // 기존 마커를 초기화
  filteredBanks.value = banks.value.filter(place => {
    if (selectedOption.value === '모든 은행') {
      return true;
    } else {
      return place.place_name.includes(selectedOption.value);
    }
  });
  filteredBanks.value.forEach(place => {
    addMarker(place);
  });
};

let markers = [];
const addMarker = (place) => {
  const marker = new window.kakao.maps.Marker({
    map: map,
    position: new window.kakao.maps.LatLng(place.y, place.x),
    title: place.place_name
  });
  markers.push(marker);
  
  window.kakao.maps.event.addListener(marker, 'click', () => {
    const infowindow = new window.kakao.maps.InfoWindow({
      content: `<div style="padding:5px;">${place.place_name}</div>`
    });
    infowindow.open(map, marker);
  });
};

const clearMarkers = () => {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
};

watch(selectedOption, () => {
  filterBanks();
});
</script>



<style scoped>
.container {
  width: 90%;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
}

.main {
  display: flex;
  width: 100%;
  justify-content: space-between;
  background-color: #f2f2f2;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-top: 20px;
}

.search-panel {
  width: 30%;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ddd;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.map-container {
  width: 65%;
  height: 450px;
  border: 1px solid #ddd;
  flex-grow: 1;
  margin: 0px 20px;
}

#map {
  width: 100%;
  height: 100%;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

select,
button {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  margin-top: 10px;
}

button:hover {
  background-color: #2e8531;
}

div.bank-list {
  margin: 50px 0px;
}

table {
  width: 100%;
  border: 1px solid black;
  border-collapse: collapse;
}

thead {
  background-color: #f4fff4;
}

th,
td {
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 1em;
}

th.first {
  width: 7%;
}

th.second {
  width: 35%;
}
</style>