tinymce.init({
    selector: "textarea",
    theme: "modern",
    content_css: "//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css",
    height: 500,
    plugins: [
    "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
    "table directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
    ],
    toolbar1: "bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | formatselect fontselect fontsizeselect | print fullscreen restoredraft preview | visualchars visualblocks nonbreaking | insertdatetime ",
    toolbar2: "searchreplace | bullist numlist | outdent indent blockquote | undo redo | link unlink anchor image media code | table | hr removeformat | subscript superscript | charmap emoticons example ",
    fontsize_formats: '8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt',
    menubar: false,
    browser_spellcheck: true,
    height : 200,
    setup: function(ed) {
        ed.addButton('example', {
            text: 'Insert',
            icon: 'code',
            context: 'tools',
            onclick: function() {
                ed.windowManager.open({
                    title: 'Insert Code',
                    width: 300,
                    height: 80,
                    body: [
                        {type: 'listbox', name: 'type', label: '','values': [
                            {text: 'HTML', value: 'html'},
                            {text: 'Ruby', value: 'ruby'},
                            {text: 'PHP', value: 'php'},
                            {text: 'JS', value: 'javascript'}
                        ]}
                    ],
                    onsubmit: function(e) {
                        ed.insertContent('<pre><code class="'+e.data.type+'">CODE</code></pre>');
                    }
                });
            }
        });
    }
});