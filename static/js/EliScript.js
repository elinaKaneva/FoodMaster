function autocomplete_food(el,url){
    var ajaxData;

    $(el).autocomplete({
        source: function( request, response ) {
            $.ajax({
                method: "GET",
                url: url,
                data: { "lookFor": $( el ).val() },
                success: function( data ) {
                    console.log(data);
                    ajaxData = data;
                    response( data.foods );
                },
            });

        },
        minLength: 1,
        select: function(event, ui){
            console.log(ajaxData);
        }

    });
}