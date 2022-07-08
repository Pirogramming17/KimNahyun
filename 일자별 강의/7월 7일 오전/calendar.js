const date = new Date(); // 현재 날짜 객체 만들기 방법
const date2 = new Date(2022, 8, 7); //지정 날짜 객체 만들기 방법

/*
console.log(date);
console.log(date2);
*/

const viewYear = date.getFullYear(); //2022
const viewMonth = date.getMonth(); //7 -> 실제로는 6이 나옴
const viewDate = date.getDate(); //7
const viewDay = date.getDay(); //0 1 2 3 4 5 6 > 일 월 화 수 목 금 토 //4 : 목

/*
console.log(viewYear)
console.log(viewMonth)
console.log(viewDate)
console.log(viewDay)
*/

//이번 달 마지막 날짜 가져오기
const thisLast = new Date(viewYear, viewMonth + 1, 0); // 지정 날짜 객체 만들기
const thisDate = thisLast.getDate(); //31
const thisDay = thisLast.getDay(); //0

//저번 달 마지막 날짜 가져오기
const prevLast = new Date(viewYear, viewMonth, 0);
const prevDate = prevLast.getDate(); //30
const prevDay = prevLast.getDay(); // 4

/*
console.log(thisLast);
console.log(thisDate);
console.log(thisDay);

console.log(prevLast);
console.log(prevDate);
console.log(prevDay);
*/

//전체 날짜를 만들기 위한 배열 만들기
//thisDates[0 1 2 3 4 ... 29 30 31]
const prevDates = [];
const thisDates = [...Array(thisDate + 1).keys()].slice(1);
const nextDates = [];

//6 = 토요일, 전달 마지막 요일이 토요일일 경우 그릴 필요가 없다!
// 이전 달 날짜를 만들어주는 코드!
//unshift는 배열을 거꾸로 앞으로 넣어주는 메소드
// prevDate [26 27 28 29 30]
if (prevDay !== 6) {
  for (let i = 0; i < prevDay + 1; i++) {
    prevDates.unshift(prevDate - i);
  }
}

//다음 달 날짜를 가진 배열 채우기
//push는 객체를 차례대로 넣어주는 메소드
//nextDates[1 2 3 4 5 6]
for (let i = 1; i < 7 - thisDay; i++) {
  nextDates.push(i);
}

//하나의 날짜들로 합쳐주는 과정
const dates = prevDates.concat(thisDates, nextDates);

//console.log(dates);

//html에 dates div 배열을 새롭게 만들어주는 과정
dates.forEach((date, i) => {
  dates[i] = `<div class= "dates">${date}</div>`;
});

//console.log(dates);

//Dates 그리기
document.querySelector(".dates").innerHTML = dates.join("");
