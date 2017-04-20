var data = [
    [0, 4, "Good night", 'bed'], 
    [5, 11, "Good morning", 'coffee'],          //Store messages in an array
    [12, 17, "Good afternoon", 'sun-o'],
    [18, 21, "Good evening", 'cloud'],
    [21, 24, "Good night", 'moon-o']
];

var updateTitle = function(hr){
    for(var i = 0; i < data.length; i++){
        if(hr >= data[i][0] && hr <= data[i][1]){
            console.log(data[i][2]);
            $('#title').html(data[i][2] + ' <i class="fa fa-'+data[i][3]+'" aria-hidden="true"></i>')
        }
    }
}

updateTitle(new Date().getHours());
