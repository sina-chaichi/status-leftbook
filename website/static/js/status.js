status={
  init: function(){

    $('.btn-secondary').on('click', function(){
      likePost(this);
    });

    function likePost(thumb){
        // Visual like button highlighting
        $(thumb).toggleClass('btn-like-post')

        // route: /like/(id)
        // Take the index of the current like-button and add
        // 1 to it (so it starts at 1) to match the primary-key
        // of the database

        id = $('.btn-secondary').index(thumb)+1
        var url = id.toString() + '/like/'
        $.ajax({
          url: url,
          data: { csrfmiddlewaretoken: '{{ csrf_token }}' },
          method: 'POST',
          success: function(){
          }
        })

    }

  }
}
