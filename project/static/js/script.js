$(document).on("ready page:change", function() {
  $('[data-toggle="tooltip"]').tooltip();
  $("#add").click(function(){
    if($('#link').val() != ''){
      $("#load").show();
    }
  });
})

$(".alert-success").fadeTo(3000, 500).slideUp(500, function(){
  $(".alert-success").alert('close');
});

$(".alert-danger").fadeTo(3000, 500).slideUp(500, function(){
  $(".alert-danger").alert('close');
});