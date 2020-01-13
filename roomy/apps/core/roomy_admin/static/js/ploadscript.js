$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
    $("table").each(function() { // invert tr and td
        var $this = $(this);
        var newrows = [];
        $this.find("tr").each(function(){
            var i = 0;
            $(this).find("td, th").each(function(){
                i++;
                if(newrows[i] === undefined) { newrows[i] = $("<tr></tr>"); }
                if(i == 1)
                    newrows[i].append("<th>" + this.innerHTML  + "</th>");
                else
                    newrows[i].append("<td>" + this.innerHTML  + "</td>");
            });
        });
        $this.find("tr").remove();
        $.each(newrows, function(){
            $this.append(this);
        });
    });

    var isMouseDown = false,
        isHighlighted;

    $("#schedule-table input:checkbox").click(function() {
        return false;
    });
    $("#schedule-table td:not(:first-child)")
        .mousedown(function() {
            isMouseDown = true;
            $(this).toggleClass("highlighted");
            isHighlighted = $(this).hasClass("highlighted");
            $(this).find("input:checkbox").prop("checked", isHighlighted);
            // console.log($(this).find("input:checkbox").prop("checked"));
            // console.log($(this).find("input:checkbox").prop("value"));
            return false;
        })
        .mouseover(function() {
            if(isMouseDown) {
                $(this).toggleClass("highlighted", isHighlighted);
                $(this).find("input:checkbox").prop("checked", isHighlighted);
                // console.log($(this).find("input:checkbox").prop("checked"));
                // console.log($(this).find("input:checkbox").prop("value"));
            }
        })
        .bind("selectstart", function() {
            return false;
        })
    
    $(document).mouseup(function() {
        isMouseDown = false;
    });
});