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
if (!Array.prototype.indexOf) {
    Array.prototype.indexOf = function(obj, start) {
         for (var i = (start || 0), j = this.length; i < j; i++) {
             if (this[i] === obj) { return i; }
         }
         return -1;
    }
}


(function($){
    if ($ && $.bugrecord) {
        return;
    }

    var AJAX_URL = '/ho600_lib/ajax/';
    var CSRFMIDDLEWARETOKEN;
    $.bugrecord = function (ajax_url, csrfmiddlewaretoken) {
        if (ajax_url) {
            AJAX_URL = ajax_url;
        }
        if (csrfmiddlewaretoken) {
            CSRFMIDDLEWARETOKEN = csrfmiddlewaretoken;
        }
        var d = {
            solvedOrQuit: '',
            clear: '',
            search: ''
        }
        d['solvedOrQuit'] = function () {
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
        };
        d['search'] = function () {
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
                $('.solvedOrQuit', $tbody).click(d['solvedOrQuit']);
            }, 'json');
        };
        d['clear'] = function () {
            $('#id_code').val('');
            $('#id_start_date').val('');
            $('#id_end_date').val('');
            $('#id_is_solved').val('');
            $('#id_type-option').val('');
            $('#id_request_url-option').val('');
            $('#id_file_name-option').val('');
        };
        return d;
    }
}) ($);


(function ($) {
    $.ho600_lib = function (DEBUG) {
        DEBUG = DEBUG ? DEBUG : false;
        var d = {
            convert_tastypie_datetime: function (s) {
                var re = new RegExp('^([0-9]+)-([0-9]+)-([0-9]+).([0-9]+):([0-9]+):([0-9]+)(\.?[0-9]*)$');
                var list = re.exec(s);
                if (list) {
                    return list[1]+'-'+list[2]+'-'+list[3]+' '+list[4]+':'+list[5]+':'+list[6];
                } else {
                    var re = new RegExp('^([0-9]+)-([0-9]+)-([0-9]+)$');
                    var list = re.exec(s);
                    return list[1]+'-'+list[2]+'-'+list[3]+' 00:00:00';
                }
            },
            get_debug: function () {
                return DEBUG;
            },
            error_object: function () {
                if (DEBUG && window.console && console.log) {
                    try {
                        throw Error('');
                    } catch (err) {
                        return err;
                    }
                }
            },
            debug_print: function (v, err) {
                if (DEBUG && window.console && console.log) {
                    if($.browser.chrome) {
                        var prefix = '(None) ';
                        if (err) {
                            var line = err.stack.split('\n')[3];
                            var re = new RegExp('at ([^ ]+) (.+):([0-9]+):([0-9]+)');
                            var list = re.exec(line);
                            if (list) {
                                var function_name = list[1];
                                var file_name = $.url(list[2].replace('(', '')).attr('file');
                                var line_number = list[3];
                                var word_number = list[4];
                                var prefix = '(' + [file_name, function_name, line_number, word_number].join(':') + ') ';
                            }
                        }
                        console.log(prefix+v);
                    }
                }
            },
            get_resource_uri_from_xhr: function (xhr) {
                var $url = $.url(xhr.getResponseHeader('Location'));
                var resource_uri = $url.attr('path');
                return resource_uri;
            }
        };
        d['dp'] = d.debug_print;
        d['get_uri'] = d.get_resource_uri_from_xhr;
        d['er'] = d.error_object;
        d['debug'] = d.get_debug;
        d['ctd'] = d.convert_tastypie_datetime;
        return d;
    };
}) ($);