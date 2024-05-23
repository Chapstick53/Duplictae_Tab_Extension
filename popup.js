document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('duplicate-tab').addEventListener('click', function () {
      chrome.runtime.sendMessage({ action: "duplicate-tab" });
    });
  });
  