tinymce.init({
    selector: "textarea",
    height: 500,
    plugins: [
    "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
    "table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
    ],
    toolbar1: "bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | ltr rtl | styleselect formatselect fontselect fontsizeselect ",
    toolbar2: "cut copy paste | searchreplace | bullist numlist | outdent indent blockquote | undo redo | link unlink anchor image media code",
    toolbar3: "table | hr removeformat | subscript superscript | charmap emoticons | print fullscreen | spellchecker | visualchars visualblocks nonbreaking template pagebreak restoredraft | forecolor backcolor | insertdatetime preview",
    fontsize_formats: '8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt',
    menubar: false,

});