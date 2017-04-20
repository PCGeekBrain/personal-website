var data = [
    [0, 4, "Good night", 'moon-o'], 
    [5, 11, "Good morning", 'sun-o'],          //Store messages in an array
    [12, 17, "Good afternoon", 'cloud'],
    [18, 24, "Good night", 'moon-o']
],
    hr = new Date().getHours();

for(var i = 0; i < data.length; i++){
    if(hr >= data[i][0] && hr <= data[i][1]){
        console.log(data[i][2]);
        $('#title').html(data[i][2] + ' <i class="fa fa-'+data[i][3]+'" aria-hidden="true"></i>')
    }
}