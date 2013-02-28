/*
# Copyright (c) 2011, ho600.com
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#     Redistributions in binary form must
#     reproduce the above copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other materials provided
#     with the distribution.
#
#     Neither the name of the ho600.com nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
var AJAX_URL = '/ho600_lib/ajax/';

function solvedOrQuit () {
    var $td = $(this).parent();
    var bug_kind_id = $td.attr('_id');
    var is_single_bug_kind =$td.attr('is_single_bug_kind');
    $.post(AJAX_URL, {submit: 'solvedOrQuit', csrfmiddlewaretoken: CSRFMIDDLEWARETOKEN, bug_kind_id: bug_kind_id}, function(json){
        if (is_single_bug_kind){
            window.location.reload();
        }else{
            $td.parent().remove();
        }
        var total_count = Number($('#id_total_count').text())-1;
        $('#id_total_count').text(total_count);
        if (total_count > 1){
            $('#id_pluralize').text('s');
        }else{
            $('#id_pluralize').text('');
        }
    }, 'json');
}


function search () {
    var code = $('#id_code').val().toUpperCase();
    var start_date = $('#id_start_date').val();
    var end_date = $('#id_end_date').val();
    var is_solved = $('#id_is_solved').val();
    var type = $('#id_type-option').val();
    var request_url = $('#id_request_url-option').val();
    var file_name = $('#id_file_name-option').val();
    if (code && (start_date || end_date || is_solved || type || request_url || file_name)) {
        alert('"Bug cude" could not mixed with other option!');
        return false;
    }

    $.post(AJAX_URL, {submit: 'search', csrfmiddlewaretoken: CSRFMIDDLEWARETOKEN, code: code,
        start_date: start_date, end_date: end_date, is_solved: is_solved, type: type,
        request_url: request_url, file_name: file_name}, function(json){
        $('#id_no_search').text('');
        $('#id_total_count').text(json['total_count']);
        if (json['total_count'] > 1){
            $('#id_pluralize').text('s');
        }else{
            $('#id_pluralize').text('');
        }
        var $tbody = $('#id_bug_kinds tbody');
        $tbody.html('');
        for (var i=0; i<json['bug_kinds'].length; i++){
            var row = json['bug_kinds'][i];
            if ((i+1)%2){
                var tr_class = 'odd';
            } else {
                var tr_class = 'even';
            }
            var tr = '<tr class="'+tr_class+'" title="Note: '+row['note']+'">';
            tr += '<td>'+(i+1)+'</td>';
            tr += '<td><a target="bug_kind_'+row['_id']+'" href="'
                +AJAX_URL+'../bugkind/'+row['_id']+'/">'+row['type']+'</a></td>';
            tr += '<td title="'+row['request_url']+'">';
            if (row['request_url'].length > 40){
                tr += '... '+row['request_url'].slice(12, 40)+' ...';
            } else {
                tr += row['request_url'];
            }
            tr +='</td>';
            tr += '<td title="'+row['file_name']+'">';
            if (row['file_name'].length > 40){
                tr += '... '+row['file_name'].slice(12, 40)+' ...';
            } else {
                tr += row['file_name'];
            }
            tr +='</td>';
            tr += '<td>'+row['line_no']+'</td>';
            if (row['is_solved']){
                tr += '<td>True</td>';
            } else {
                tr += '<td class="notice">False</td>';
            }
            tr += '<td>'+row['create_time']+'</td>';
            tr += '<td>';
            for (var j=0; j<row['lastest_10_bug_codes'].length; j++){
                var code = row['lastest_10_bug_codes'][j];
                tr += '<a target="bug_page_'+code+'" href="'
                    +AJAX_URL+'../bugpage/'+code+'/">'+code+'</a>, ';
            }
            tr += '</td>';
            if (row['is_solved']){
                tr += '<td _id="'+row['_id']+'"><button type="button" class="solvedOrQuit ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" role="button" aria-disabled="false"><span class="ui-button-text">Not Solved</span></button></td>';
            } else {
                tr += '<td _id="'+row['_id']+'"><button type="button" class="solvedOrQuit ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" role="button" aria-disabled="false"><span class="ui-button-text">Solved</span></button></td>';
            }
            tr += '</tr>';
            $tbody.append($(tr));
        }
        $('.solvedOrQuit', $tbody).click(solvedOrQuit);
    }, 'json');
}


function clear () {
    $('#id_code').val('');
    $('#id_start_date').val('');
    $('#id_end_date').val('');
    $('#id_is_solved').val('');
    $('#id_type-option').val('');
    $('#id_request_url-option').val('');
    $('#id_file_name-option').val('');
}


$(document).ready(function(){
    $('.clear').click(clear);
    $('.search').click(search);
    $('.solvedOrQuit').click(solvedOrQuit);

    $.datepicker.setDefaults({dateFormat: 'yy-mm-dd'});
    $('input.date').each(function() {
        $(this).datepicker({
            changeMonth: true,
            changeYear: true
        });
    });

    $('img#loading').ajaxStop(function(){
        var $img = $(this);
        if($img.attr('status') != 'disable'){
            $('#id_body').css('opacity', 1);
            $img.hide();
        }
    });
    $('img#loading').ajaxStart(function(){
        var $img = $(this);
        if($img.attr('status') != 'disable'){
            $('#id_body').css('opacity', 0.25);
            $img.css('z-index', 10000).show();
        }
    });
});


$(document).ajaxError(function(envent, request, settings){
    $('#id_body').append($('<div id="id_ajaxErrorDialog"></div>'));
    var $ajaxErrorDialog = $('#id_ajaxErrorDialog', $('#id_body'));
    if (request['status'] == '0'){
        var title = 'Connection Error';
        var message = '<p>It has no network betweed You and us.</p><p>You can try to browse <a href="http://www.google.com/" target="_blank">Google</a> to check your network status.<br/>Please try again later!</p>';
    } else {
        var title = 'Runtime Error';
        if (request['status'] == '500') {
            var code = request['responseText'];
            var link = '<a href="'+AJAX_URL+'../bugpage/'+code+'/" target="_blank">'+code+'</a>';;
            var message = 'Web program has a problem[Error code: '+link+'].<br/>This error report has been accepted by programmer.<br/>Please try again later!';
        } else if (request['status'] == '404') {
            var list = request['responseText'].split('<>');
            var path = list[0];
            var code = list[1];
            var message = 'Could not request ' + path + ' [Error code: '+code+']<br/>This error report has been accepted by programmer.<br/>Please try again later!';
        } else if (request['status'] == '403') {
            var code = request['responseText'];
            var message = 'System deny your request, because <span class="notice">[ '+code+' ]</span>';
        } else if (request['status'] == '200') {
            var message = request['responseText'];
        } else {
            var code = request['responseText'];
            var message = 'Web program has a problem[Error code: '+request['status']+','+code+'].<br/>This error report has been accepted by programmer.<br/>Please try again later!';
        }
    }
    $ajaxErrorDialog.html(message).dialog({
        title: title,
        modal: true,
        overlay: {opacity: 0.8, background: "black"},
        buttons: {
            'Close': function(){
                $ajaxErrorDialog.dialog('close');
            }
        },
        width: 500
    });
});