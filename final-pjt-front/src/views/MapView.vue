<template>
  <div class="container">
    <h1>은행 찾기</h1>
    <div class="main">
      <div class="search-panel">
        <form @submit.prevent="searchBanks">
          <div class="form-group">
            <label for="city">광역시/도</label>
            <select v-model="selectedCity" id="city">
              <option v-for="city in cities" :key="city.name" :value="city">
                {{ city.name }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="district">시/군/구</label>
            <select id="district" v-model="selectedDistrict">
              <option v-for="district in selectedCity.districts" :key="district" :value="district">
                {{ district }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="bank">은행</label>
            <select id="bank" v-model="selectedBank">
              <option v-for="bank in banks" :key="bank" :value="bank">
                {{ bank }}
              </option>
            </select>
          </div>
          <button type="submit">찾기</button>
        </form>
      </div>
      <div class="map-container">
        <div id="map"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';

const kakaoMapApiKey = import.meta.env.VITE_KAKAO_MAP_API_KEY;
console.log('사용 중인 카카오 API 키:', kakaoMapApiKey);

const cities = ref([
  { name: '서울특별시', districts: ['전체', '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'] },
  { name: '부산광역시', districts: ['전체', '강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'] },
  { name: '대구광역시', districts: ['전체', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구'] },
  { name: '인천광역시', districts: ['전체', '강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군'] },
  { name: '광주광역시', districts: ['전체', '광산구', '남구', '동구', '북구', '서구'] },
  { name: '대전광역시', districts: ['전체', '대덕구', '동구', '서구', '유성구'] },
  { name: '울산광역시', districts: ['전체', '남구', '동구', '북구', '울주군', '중구'] }
]);

const banks = ref([]);
const selectedCity = ref(cities.value[0]);
const selectedDistrict = ref('강남구');
const selectedBank = ref('국민은행');

let map, geocoder;

onMounted(async () => {
  console.log('onMounted 실행됨');
  const scriptUrl = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${kakaoMapApiKey}&libraries=services&autoload=false`;
  console.log('스크립트 URL:', scriptUrl);

  const script = document.createElement('script');
  script.src = scriptUrl;
  script.onload = () => {
    console.log('카카오 맵 스크립트 로드됨');
    if (window.kakao && window.kakao.maps) {
      window.kakao.maps.load(() => {
        console.log('카카오 맵 로드됨', window.kakao.maps);
        const container = document.getElementById('map');
        const options = {
          center: new window.kakao.maps.LatLng(37.5665, 126.9780), // 초기 위치 (서울)
          level: 3 // 초기 줌 레벨
        };
        map = new window.kakao.maps.Map(container, options);
        geocoder = new window.kakao.maps.services.Geocoder();
        searchBanks(); // 초기 검색
      });
    } else {
      console.error('카카오 맵 객체가 없습니다.');
    }
  };
  script.onerror = () => {
    console.error('카카오 맵 스크립트 로드 실패');
  };
  document.head.appendChild(script);

  // 은행 목록 가져오기
  try {
    const response = await axios.get('http://localhost:8000/api/banks/');
    banks.value = response.data;
  } catch (error) {
    console.error('은행 목록을 가져오는 데 실패했습니다:', error);
  }
});

watch(selectedCity, () => {
  selectedDistrict.value = '전체';
  searchBanks();
});

const searchAddress = () => {
  if (!geocoder) return;

  const fullAddress = `${selectedCity.value.name} ${selectedDistrict.value}`;
  console.log(`검색 주소: ${fullAddress}`);
  geocoder.addressSearch(fullAddress, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const coords = new window.kakao.maps.LatLng(result[0].y, result[0].x);
      map.setCenter(coords);
    } else {
      console.error('주소 검색 실패:', status);
    }
  });
};

const searchBanks = () => {
  if (!map) return;

  const places = new window.kakao.maps.services.Places();
  const keyword = `${selectedCity.value.name} ${selectedDistrict.value} ${selectedBank.value}`;
  console.log(`검색 키워드: ${keyword}`);

  places.keywordSearch(keyword, (result, status) => {
    if (status === window.kakao.maps.services.Status.OK) {
      const bounds = new window.kakao.maps.LatLngBounds();
      map.markers = [];

      for (let i = 0; i < result.length; i++) {
        const coords = new window.kakao.maps.LatLng(result[i].y, result[i].x);
        const marker = new window.kakao.maps.Marker({
          map: map,
          position: coords,
        });

        bounds.extend(coords);
        map.markers.push(marker);
      }

      map.setBounds(bounds);
    } else {
      // alert('검색 결과가 없습니다.');
    }
  });
};
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
}
</style>