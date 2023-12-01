$(document).ready(function () {
    // sidenav initialisation
    $('.sidenav').sidenav();

    // modal initialisation
    $('.modal').modal();

    // datepicker initialisation
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        i18n: { done: "Select" }
    }
    );

    // select initialisation
    $('select').formSelect();

    //collapsible initialisation
    $('.collapsible').collapsible();
});
