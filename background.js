chrome.runtime.onInstalled.addListener(function () {
  chrome.commands.onCommand.addListener(function (command) {
    if (command === 'duplicate-tab') {
      duplicateTab();
    }
  });

  chrome.action.onClicked.addListener(function (tab) {
    duplicateTab();
  });

  function duplicateTab() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      const currentTab = tabs[0];
      chrome.tabs.duplicate(currentTab.id);
    });
  }
});
