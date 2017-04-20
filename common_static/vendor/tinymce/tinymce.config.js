tinymce.init({
    selector: "textarea",
    height: 500,
    plugins: [
    "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
    "table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
    ],
    toolbar1: "bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | formatselect fontselect fontsizeselect | print fullscreen restoredraft preview | visualchars visualblocks nonbreaking | insertdatetime ",
    toolbar2: "searchreplace | bullist numlist | outdent indent blockquote | undo redo | link unlink anchor image media code | table | hr removeformat | subscript superscript | charmap emoticons insertdatetime ",
    fontsize_formats: '8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt',
    menubar: false,
    browser_spellcheck: true,
    height : 200,
});