$(document).ready(function() {

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function(e) {
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Você deseja mesmo deletar este Item da lista?')

        if(result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});