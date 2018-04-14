$('document').ready(function() {
  let markasdone = $('#markasdone');
  markasdone.on('click', ()=>{
    markasdone.html('Done!');
    markasdone.removeClass('btn-primary');
    // markasdone.addClass('btn-success');
    markasdone.attr('disabled', 'disabled');
  });
});
