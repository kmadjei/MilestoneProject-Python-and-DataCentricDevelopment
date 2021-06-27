$(document).ready(function(){
    // Materialize-css elements initialization
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
    $('.modal').modal();

    // Adds new line for Preparation steps
    let step = 1;
    $('#add_prep_step').click(function(){
        //console.log($('#recipe-form div.row').last().children().last().text())
        $('#recipe-form div.row').eq(2).children().last().append(`
            <a class="delete_step btn-floating btn-small waves-effect red tooltipped" data-position="left" data-tooltip="Delete"><i class="material-icons">delete_forever</i></a>
            <textarea id="prep${step +=1}" name="prep${step}" class="validate materialize-textarea" required></textarea>
        `);

       // removes new line added when trash icon is clicked
        $('.delete_step').click(function(){
            $(this).next().remove();
            $(this).remove();
        });
    });

    

    //$('#add_prep_step'). $("p").after()("Some appended text.");

});