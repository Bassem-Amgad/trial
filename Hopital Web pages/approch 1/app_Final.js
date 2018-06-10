(function(){
	// initialize Firebase
	var config = {
		apiKey: "AIzaSyCj9gVUPtRzSHpDNL8lj81BplQ9_IZRjn4",
		authDomain: "reception-ef20c.firebaseapp.com",
		databaseURL: "https://reception-ef20c.firebaseio.com",
		projectId: "reception-ef20c",
		storageBucket: "reception-ef20c.appspot.com",
		messagingSenderId: "711989019574"
		  };
	firebase.initializeApp(config);
	
	// Get elements
	const preinfo= document.getElementById('information');
	
	document.getElementById("myBtn").addEventListener("click", function( event ) {  
    event.preventDefault();
	var dbRefObject = firebase.database().ref(document.getElementById('tag').value);
	dbRefObject.on('value',snap => 
	 {
		preinfo.innerHTML = contactHtmlFromObject(snap.val());	
	});
	}, false);
	
	document.getElementById("Clear").addEventListener("click", function( clear_event ) {  
    clear_event.preventDefault();
	document.getElementById('tag').value ='';
	preinfo.innerHTML='';
	}, false);
		
function contactHtmlFromObject(ID){
  var html = '';
  html += '<li class="list-group-item ID">';
    html += '<div>';
      html += '<p class="lead">'+ID.Name+'</p>';
      html += '<p>Address: '+ID.Address+'</p>';
	  html += '<p>Age: '+ID.Age+'</p>';
    html += '</div>';
  html += '</li>';
  return html;
}


}());