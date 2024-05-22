import { defineStore } from "pinia";
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export const useChartStore = defineStore("chart", () => {
  const drawChart = (chartId, products, label1, label2) => {
    const ctx = document.getElementById(chartId).getContext('2d');
    const labels = products.map(p => p.deposit.fin_prdt_nm || p.saving.fin_prdt_nm);
    const data1 = products.map(p => p.options[0]?.intr_rate || 0);  // 첫 번째 옵션의 금리를 사용
    const data2 = products.map(p => p.options[0]?.intr_rate2 || 0); // 첫 번째 옵션의 최고 우대 금리를 사용

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels,
        datasets: [
          {
            label: label1,
            data: data1,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          },
          {
            label: label2,
            data: data2,
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }
        ]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  };

  return { drawChart };
});
