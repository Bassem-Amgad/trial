(function(){
	// initialize Firebase
	var config = {
		apiKey: "AIzaSyAV5JY0NhGe8CoOyjKk4nXHRBkNLNbYN6k",
		authDomain: "registration-7cc3f.firebaseapp.com",
		databaseURL: "https://registration-7cc3f.firebaseio.com",
		projectId: "registration-7cc3f",
		storageBucket: "registration-7cc3f.appspot.com",
		messagingSenderId: "356858584491"
		  };
	firebase.initializeApp(config);
	
	// Get elements
	const pretrial= document.getElementById('information');
	// create reference
	var dbRefObject = firebase.database().ref();
	
	document.getElementById("myBtn").addEventListener("click", function( event ) {  
    event.preventDefault();
	var dbChildRefObject = firebase.database().ref().child('List/' +document.querySelector('#Tag').value);
	dbChildRefObject.on('value',snap => 
	 {
		pretrial.innerHTML = contactHtmlFromObject(snap.val());	
	});
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