
function notify(title, message, iconUrl){
  iconUrl = typeof iconUrl !== 'undefined' ? iconUrl : "icon.png"; 
  chrome.notifications.create("", {
    "type": "basic", 
    "iconUrl": iconUrl,
    "title": title, 
    "message": message
  }, function(){});
};

      
notify("test", "test" );
