let examCancelled = false;
let examSubmitted = false;
const totalSeconds = totalQuestions * 60;
let remainingSeconds = totalSeconds;

// Show timer countdown
function updateTimerDisplay() {
  let minutes = String(Math.floor(remainingSeconds / 60)).padStart(2, '0');
  let seconds = String(remainingSeconds % 60).padStart(2, '0');
  document.getElementById("timer").innerText = `${minutes}:${seconds}`;
}

// Countdown logic
function startTimer() {
  updateTimerDisplay();
  const timerInterval = setInterval(() => {
    if (examSubmitted) {
      clearInterval(timerInterval);
      return;
    }
    remainingSeconds--;
    if (remainingSeconds <= 0) {
      clearInterval(timerInterval);
      document.getElementById("exam-form").submit(); // auto-submit
    }
    updateTimerDisplay();
  }, 1000);
}

// Tab switch detection
document.addEventListener("visibilitychange", function () {
  if (document.visibilityState === "hidden" && !examCancelled && !examSubmitted) {
    examCancelled = true;
    alert("❌ Tab switch detected. Exam cancelled.");
    window.location.href = "/logout";
  }
});

function startExam() {
  document.querySelector(".rules-box").style.display = "none";
  document.getElementById("exam-content").style.display = "block";
  startTimer();
}

document.getElementById("exam-form").addEventListener("submit", function () {
  examSubmitted = true;
});
