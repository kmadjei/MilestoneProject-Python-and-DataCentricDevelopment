$(document).ready(function(){
    // Materialize-css elements initialization
    $(".sidenav").sidenav({edge: "right"});
    $('.tooltipped').tooltip();
    $('.modal').modal();

    // Adds new line for Preparation steps
    let step = 1;
    $('#add_prep_step').click(function(){
        //console.log($('#recipe-form div.row').last().children())
        $('#add-recipe-form div.row').last().children().last().append(`
            <a class="delete_step btn-floating btn-small waves-effect red tooltipped" data-position="left" data-tooltip="Delete"><i class="material-icons">delete_forever</i></a>
            <textarea id="prep${step +=1}" name="prep${step}" class="validate materialize-textarea" required></textarea>
        `);
        
       // removes new line added when trash icon is clicked
        $('.delete_step').click(function(){
            $(this).next().remove();
            $(this).remove();
        });
    });
    
    // add-recipe-form validation
    $('#add-recipe-form').submit(function(){
        //console.log($('#add-recipe-form input'));
        if ($('#recipe_name').val().trim() == '') {
            alert('Make sure all required fields are filled out.');
            return false;
        }

        if ($('#img_url').val().trim() == '') {
            alert('Make sure all required fields are filled out.');
            return false;
        }

        if ($('#author').val().trim() == '') {
            alert('Make sure all required fields are filled out.');
            return false;
        }

        if ($('#ingredients').val().trim() == '') {
            alert('Make sure all required fields are filled out.');
            return false;
        }

        if ($('#prep').val().trim() == '') {
            alert('Make sure all required fields are filled out.');
            return false;
        }
    
    });

    
    
    
});