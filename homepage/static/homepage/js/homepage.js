//Data [starting hour, ending hour, message, fa icon name]
var data = [
    [0, 4, "Good night", 'bed'], 
    [5, 11, "Good morning", 'coffee'],          //Store messages in an array
    [12, 17, "Good afternoon", 'sun-o'],
    [18, 21, "Good evening", 'cloud'],
    [21, 24, "Good night", 'moon-o']
];
//split to function to allw automated test on website TODO automated test
var updateTitle = function(hr){
    for(var i = 0; i < data.length; i++){ // for every item in the array
        if(hr >= data[i][0] && hr <= data[i][1]){
            $('#title').html(data[i][2] + ' <i class="fa fa-'+data[i][3]+'" aria-hidden="true"></i>')
            return; //Should imporve performance
        }
    }
}
updateTitle(new Date().getHours());
