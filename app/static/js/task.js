$(document).ready(function() {
  $(':checkbox').on('click', changetasksStatus);
});

function changetasksStatus() {
  if ($(this).is(':checked')) {
    putNewStatus($(this).data('tasks-id'), true);
  } else {
    putNewStatus($(this).data('tasks-id'), false);
  }
}
