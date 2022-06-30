//1
const duration = 30;
let lapse = 0;
let intervalID;

//2
const progressEl = document.querySelector(".progress");
const lapseEl = document.querySelector(".lapse .seconds");
const remainingEl = document.querySelector(".remaining .seconds");

function fillZero(num) {
  return String(num).padStart(2, "0");
}

//3
remainingEl.innerText = fillZero(duration);

const playBtn = document.querySelector(".play-btn");
const pauseBtn = document.querySelector(".pause-btn");

function changeBtn() {
  playBtn.classList.toggle("hidden");
  pauseBtn.classList.toggle("hidden");
}

playBtn.addEventListener("click", function () {
  //4
  changeBtn();

  if (!lapse) {
    progressEl.style.width = 0;
    lapseEl.innerText = fillZero(0);
    remainingEl.innerText = fillZero(duration);
  }

  //6
  intervalID = setInterval(
    function () {
      //8
      progressEl.style.width = `${(100 * ++lapse) / duration}%`;
      lapseEl.innerText = String(lapse).padStart(2, "0");
      remainingEl.innerText = String(duration - lapse).padStart(2, "0");

      if (lapse === duration) {
        changeBtn();
        clearInterval(intervalID);
        lapse = 0;
      }
    },

    1000
  );
});

pauseBtn.addEventListener("click", function () {
  //5
  changeBtn();
  //7
  clearInterval(intervalID);
});
