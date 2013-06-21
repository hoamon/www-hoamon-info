/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
function CPM (duration) {
    this.nodes = {
        "#0": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#A', '#B', '#C', '#D']},
        "#A": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#E']},
        "#B": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#F']},
        "#C": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#G']},
        "#D": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#G', '#H']},
        "#E": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#I']},
        "#F": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#I']},
        "#G": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#End']},
        "#H": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#End']},
        "#I": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': ['#End']},
        "#End": {'duration': 0, 'es': 0, 'ef': 0, 'ls': 99999999, 'lf': 99999999, 'children': []}
    };
    for (var k in duration) {
        this.nodes[k]['duration'] = duration[k];
    }
    this.links = [
        {'type': 'FS', 'parent': '#0', 'child': '#A', 'lag': 0},
        {'type': 'FS', 'parent': '#0', 'child': '#B', 'lag': 0},
        {'type': 'FS', 'parent': '#0', 'child': '#C', 'lag': 0},
        {'type': 'FS', 'parent': '#0', 'child': '#D', 'lag': 0},
        {'type': 'FS', 'parent': '#A', 'child': '#E', 'lag': 0},
        {'type': 'FS', 'parent': '#B', 'child': '#F', 'lag': 0},
        {'type': 'FS', 'parent': '#C', 'child': '#G', 'lag': 0},
        {'type': 'FS', 'parent': '#D', 'child': '#G', 'lag': 0},
        {'type': 'FS', 'parent': '#D', 'child': '#H', 'lag': 0},
        {'type': 'FS', 'parent': '#E', 'child': '#I', 'lag': 0},
        {'type': 'FS', 'parent': '#F', 'child': '#I', 'lag': 0},
        {'type': 'FS', 'parent': '#I', 'child': '#End', 'lag': 0},
        {'type': 'FS', 'parent': '#G', 'child': '#End', 'lag': 0},
        {'type': 'FS', 'parent': '#H', 'child': '#End', 'lag': 0}
    ];
    this.forward = function () {
        var nodes = this.nodes;
        var varify = '';
        for (var i=0; i<this.links.length; i++) {
            var f = this.links[i];
            var parent = f['parent'];
            var child = f['child'];
            var es = '';
            var ef = nodes[parent]['es'] + nodes[parent]['duration'];
            if (nodes[parent]['ef'] < ef) {
                nodes[parent]['ef'] = ef;
            }
            if (f['type'] == 'FS') {
                es = nodes[parent]['ef'] + f['lag'];
                if (nodes[child]['es'] < es) {
                    nodes[child]['es'] = es;
                }
                varify += '%d,' % nodes[child]['es'];
            }
            if (f['type'] == 'SS') {
                es = nodes[parent]['es'] + f['lag'];
                if (nodes[child]['es'] < es){
                    nodes[child]['es'] = es;
                }
                varify += '%d,' % nodes[child]['ef'];
            }
            if (f['type'] == 'FF') {
                ef = nodes[parent]['ef'] + f['lag'];
                if (nodes[child]['ef'] < ef){
                    nodes[child]['ef'] = ef;
                }
                varify += '%d,' % nodes[child]['ef'];
            }
            if (f['type'] == 'SF') {
                ef = nodes[parent]['es'] + f['lag'];
                if (nodes[child]['ef'] < ef) {
                    nodes[child]['ef'] = ef;
                }
                varify += '%d,' % nodes[child]['ef'];
            }
        }
        return varify;
    };


    this.backward = function () {
        var nodes = this.nodes;
        var varify = '';
        for (var i=0; i<this.links.length; i++) {
            var f = this.links[i];
            var parent = f['parent'];
            var child = f['child'];
            var lf = '';
            var ls = nodes[child]['lf'] - nodes[child]['duration'];
            if (nodes[child]['ls'] > ls) {
                nodes[child]['ls'] = ls;
            }
            if (f['type'] == 'FS') {
                lf = nodes[child]['ls'] - f['lag'];
                if (nodes[parent]['lf'] > lf) {
                    nodes[parent]['lf'] = lf;
                }
                varify += '%d,' % nodes[parent]['lf'];
            }
            if (f['type'] == 'SS') {
                ls = nodes[child]['ls'] - f['lag'];
                if (nodes[parent]['ls'] > ls) {
                    nodes[parent]['ls'] = ls;
                }
                varify += '%d,' % nodes[parent]['ls'];
            }
            if (f['type'] == 'FF') {
                lf = nodes[child]['lf'] - f['lag'];
                if (nodes[parent]['lf'] > lf) {
                    nodes[parent]['lf'] = lf;
                }
                varify += '%d,' % nodes[parent]['lf'];
            }
            if (f['type'] == 'SF') {
                ls = nodes[child]['lf'] - f['lag'];
                if (nodes[parent]['ls'] > ls) {
                    nodes[parent]['ls'] = ls;
                }
                varify += '%d,' % nodes[parent]['ls'];
            }
        }
        return varify;
    };


    this.run = function () {
        var oldvarify = '';
        var varify = '0';
        var i = 0;
        while (oldvarify != varify && i <= 50) {
            i += 1;
            oldvarify = varify;
            varify = this.forward();
        }
        var end_node_name = this.links[this.links.length-1]['child'];
        this.nodes[end_node_name]['lf'] = this.nodes[end_node_name]['es'] + this.nodes[end_node_name]['duration'];
        this.nodes[end_node_name]['ef'] = this.nodes[end_node_name]['es'] + this.nodes[end_node_name]['duration'];

        oldvarify = '';
        varify = '0';
        var begin_node_name = this.links[0]['parent'];
        this.links.reverse();
        i = 0;
        while (oldvarify != varify && i <= 50) {
            i += 1;
            oldvarify = varify;
            varify = this.backward();
        }

        this.nodes[begin_node_name]['ls'] = this.nodes[begin_node_name]['lf'] - this.nodes[begin_node_name]['duration'];

        for (var k in this.nodes) {
            this.nodes[k]['tf'] = this.nodes[k]['lf'] - this.nodes[k]['duration'] - this.nodes[k]['es'];
            var min_lf = 99999999;
            for (var i=0; i<this.nodes[k]['children'].length; i++) {
                var child = this.nodes[this.nodes[k]['children'][i]];
                if (child['es'] < min_lf) {
                    min_lf = child['es'];
                }
            }
            this.nodes[k]['ff'] = min_lf - this.nodes[k]['duration'] - this.nodes[k]['es'];
        }
    };


    this.show = function () {
        console.log('nodes: ');
        for (var k in this.nodes) {
            console.log('\t' + k + ':');
            for (var v_k in this.nodes[k]) {
                console.log('\t\t'+v_k+': ' + this.nodes[k][v_k]);
            }
            console.log('\n');
        }
    };
    return this;
}


(function ($) {
    var contractor_number;
    function clear() {
        var $tr = $('tr:gt(0)', $('td:contains(累計進度％)').parents('table'));
        $('td:gt(0)' , $tr).text('');

        var $tr = $('tr:gt(0)', $('td:contains(當日週轉金額)').parents('table'));
        $('td:gt(0)' , $tr).text('');

        var $tr = $('tr:gt(0)', $('th:contains(趕工天期)').parents('table'));
        $('td:gt(0)' , $tr).text('');
    }
    function calculate () {
        contractor_number = /^([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])/.exec($('#input_number').val());
        if (!contractor_number) {
            alert('輸入位數須為 10 位數!!!');
            return false;
        }
        contractor_number.shift(0);
        for (var i=0; i<contractor_number.length; i++) {
            contractor_number[i] = Number(contractor_number[i]);
        }
        clear();
        cal_rational_bid();
        cal_bid_prices();
        cal_guarantee_prices();
        cal_quality_control();
        cal_pert();
    }
    function make_line (s) {
        return '<div style="line-height: 2;">□ '+s+'</div>\n';
    }
    function list_to_number(list) {
        return Number(list.join(''));
    }
    function change_number (list, postions) {
        var j = 0;
        for (var i=0; i<list.length; i++){
            if (list[i] === '') {
                list[i] = contractor_number[postions[j]-1];
                j += 1;
            }
        }
        return list;
    }
    function cal_pert () {
        var $table = $('td:contains(請依序代入貴企業的廠商代號 1 ～ 9 碼):first').parents('table');
        var i = 0;
        $('tr:eq(1) td:gt(0):lt(9)', $table).each(function () {
            $(this).text(contractor_number[i]);
            i += 1;
        })
        var i = 0;
        var cpm_duration = {};
        var durations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
        var d = '';
        $('tr:eq(2) td:gt(0):lt(9)', $table).each(function () {
            if (contractor_number[i] == 0) {
                d = 1;
            } else if (contractor_number[i] % 2 == 0) {
                d = 2;
            } else {
                d = 3;
            }
            $(this).text(d);
            cpm_duration['#'+durations[i]] = d;
            i += 1;
        })
        var cpm = new CPM(cpm_duration);
        cpm.run();
        var $table = $('th:contains(要徑工項請填 ○)').parents('table');
        for (var i=0; i<durations.length; i++){
            var key = durations[i];
            var $tr = $('td:contains('+durations[i]+')', $table).parent();
            $('td:eq(1)', $tr).text(cpm.nodes['#'+key]['es']);
            $('td:eq(2)', $tr).text(cpm.nodes['#'+key]['ef']);
            $('td:eq(3)', $tr).text(cpm.nodes['#'+key]['ls']);
            $('td:eq(4)', $tr).text(cpm.nodes['#'+key]['lf']);
            $('td:eq(5)', $tr).text(cpm.nodes['#'+key]['tf']);
            $('td:eq(6)', $tr).text(cpm.nodes['#'+key]['ff']);
            $('td:eq(7)', $tr).text((cpm.nodes['#'+key]['tf'] === 0 ? '○' : ""));
            $('td:gt(0)', $tr).css('color', 'blue');
        }
        var $table = $('td:contains(累計進度％)').parents('table');
        var prices = { '#A': 60, "#B": 180, "#C": 120, "#D": 60, "#E": 240,
            "#F": 60, "#G": 60, "#H": 60, "#I": 180 };
        var total_price = 0;
        for (var i=0; i<durations.length; i++){
            var node = durations[i];
            var duration = cpm.nodes['#'+node]['duration'];
            var es = cpm.nodes['#'+node]['es'];
            var $tr = $('td:contains('+node+')', $table).parent();
            var price_per_day = prices['#'+node] / duration;
            total_price += prices['#'+node];
            var s = 'td:gt('+es+')';
            var j = 0;
            $(s, $tr).each(function(){
                if (j < duration) {
                    $(this).text(price_per_day);
                }
                j += 1;
            });
        }
        var daysum = [];
        var sum = 0;
        var sum_list = [];
        var percent = [];
        for (var i=1; i<=16; i++) {
            var p = 0;
            $('tr:gt(0)', $table).each(function(){
                $('td:eq('+i+')', $(this)).each(function(){
                    p += Number($(this).text());
                })
            })
            daysum.push(p);
            sum += p;
            sum_list.push(sum);
            var _p = Math.round(sum/total_price*10000)/100;
            percent.push(_p);
            if (_p >= 100) {
                break;
            }
        }
        var $tr = $('td:contains(小計金額)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(daysum[i]).css('color', 'blue');
            i += 1;
        })
        var $tr = $('td:contains(累計金額)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(sum_list[i]).css('color', 'blue');
            i += 1;
        })
        var $tr = $('td:contains(累計進度％)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(percent[i]).css('color', 'blue');
            i += 1;
        })


        var $table = $('td:contains(當日週轉金額)').parents('table');
        var c_prices = { '#A': 30, "#B": 150, "#C": 90, "#D": 30, "#E": 210,
            "#F": 60, "#G": 30, "#H": 30, "#I": 150 };
        var total_price = 0;
        for (var i=0; i<durations.length; i++){
            var node = durations[i];
            var duration = cpm.nodes['#'+node]['duration'];
            var es = cpm.nodes['#'+node]['es'];
            var $tr = $('td:contains('+node+')', $table).parent();
            var price_per_day = c_prices['#'+node] / duration;
            total_price += c_prices['#'+node];
            var s = 'td:gt('+es+')';
            var j = 0;
            $(s, $tr).each(function(){
                if (j < duration) {
                    $(this).text(price_per_day);
                }
                j += 1;
            });
        }

        var $tr = $('td:contains(契約金額小計)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(daysum[i]).css('color', 'blue');
            i += 1;
        })
        var $tr = $('td:contains(累計契約金額)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(sum_list[i]).css('color', 'blue');
            i += 1;
        })

        var c_daysum = [];
        var c_sum = 0;
        var c_sum_list = [];
        for (var i=1; i<=16; i++) {
            var p = 0;
            $('tr:gt(0):lt(9)', $table).each(function(){
                $('td:eq('+i+')', $(this)).each(function(){
                    p += Number($(this).text());
                })
            })
            c_daysum.push(p+5);
            total_price += 5;
            c_sum += p + 5;
            c_sum_list.push(c_sum);
            if (c_sum >= total_price) {
                break;
            }
        }

        var $tr = $('td:contains(管理成本小計)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            if (i<cpm.nodes['#End']['es']){
                $(this).html('5').css('color', 'blue');
            }
            i += 1;
        })
        var $tr = $('td:contains(支出金額小計)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(c_daysum[i]).css('color', 'blue');
            i += 1;
        })
        var $tr = $('td:contains(累計支出金額)', $table).parent();
        var i = 0;
        $('td:gt(0)', $tr).each(function(){
            $(this).text(c_sum_list[i]).css('color', 'blue');
            i += 1;
        })
        var $tr = $('td:contains(累計契約金額)', $table).parent();
        var first = Number($('td:eq(5)', $tr).text());
        var second = Number($('td:eq('+cpm.nodes['#End']['es']+')', $tr).text()) - first;
        var $tr = $('td:contains(請款金額)', $table).parent();
        $('td:eq(6)', $tr).text(first).css('color', 'blue');
        $('td:eq('+(cpm.nodes['#End']['es']+1)+')', $tr).text(second).css('color', 'blue');

        var $tr = $('td:contains(保留款金額)', $table).parent();
        var reserve1 = first*0.05;
        var reserve2 = second*0.05;
        $('td:eq(11)', $tr).text(reserve1).css('color', 'blue');
        $('td:eq('+(cpm.nodes['#End']['es']+6)+')', $tr).text(reserve2).css('color', 'blue');

        var $tr = $('td:contains(實際撥款金額)', $table).parent();
        $('td:eq(11)', $tr).text(first*0.95).css('color', 'blue');
        $('td:eq('+(cpm.nodes['#End']['es']+6)+')', $tr).text(second*0.95+reserve1+reserve2).css('color', 'blue');

        var $_tr = $('td:contains(當日週轉金額)', $table).parent();
        var _d = 0;
        var minimal = 0;
        for (var i=1; i<=16; i++) {
            var plus = $('td:eq('+i+')', $tr).text();
            plus = plus ? Number(plus) : 0;
            var minus = c_daysum[i-1] ? c_daysum[i-1] * -1 : 0;
            _d += minus+plus;
            if (_d < minimal){
                minimal = _d;
            }
            $('td:eq('+i+')', $_tr).text(_d).css('color', 'blue');
        }
        $('#minimal').text(-1*minimal+'萬').css('color', 'blue');

        var charrette_prices = { '#A': 55, "#B": 175, "#C": 110, "#D": 55, "#E": 220,
            "#F": 65, "#G": 55, "#H": 70, "#I": 155 };
        var result = '';
        result += make_line('請依序選擇下列工項為趕工工項:');
        var charrettes = [];
        for (var k in prices) {
            var l = charrette_prices[k] + ' - ' + c_prices[k];
            var value = eval(l);
            l = k + ':' + l + ' = ' + value + '(趕工 1 天多花 '+ value + '萬元)';
            charrettes.push([value, l, k]);
        }
        charrettes.sort(function(a, b){
            return a[0] - b[0];
        });
        for (var i=0; i<charrettes.length; i++) {
            result += make_line(charrettes[i][1]);
        }
        result += make_line('<span style="color: red">P.S. 如果你的趕工 2 天方案中，存在「浮時減少天數是負值」的情況，莫驚慌、莫害怕！！！這只是代表某個工項從要徑工項變成非要徑工項而已。重點還是在工期減少上面。</span>');
        $('#charrette').html(result).css('color', 'blue');

        var old_nodes = {};
        for (var k in cpm.nodes) {
            old_nodes[k] = {
                'duration': cpm.nodes[k]['duration'],
                'tf': cpm.nodes[k]['tf']
            };
        }
        var $tables = $('th:contains(趕工天期)').parents('table');
        var paths = [['#I', '#E', '#A'],
                    ['#F', '#I', '#B'],
                    ['#C', '#G'],
                    ['#D', '#G'],
                    ['#D', '#H']];
        var nodes = cpm.nodes;
        var has_cut_day = [];

        for (var j=0; j<=1; j++) {
            for (var p_i=0; p_i<paths.length; p_i++) {
                //決定要徑
                var path = paths[p_i];
                var is_critical_path = true;
                for(var i=0; i<path.length; i++) {
                    if (nodes[path[i]]['tf'] > 0) {
                        is_critical_path = false;
                        break;
                    }
                }

                if (is_critical_path) {
                    //趕工工期
                    for(var i=0; i<path.length; i++) {
                        if (has_cut_day.indexOf(path[i]) < 0 && cpm_duration[path[i]] > 1){
                            cpm_duration[path[i]] -= 1;
                            has_cut_day.push(path[i]);
                            break;
                        }
                    }
                }
            }

            var _s = '';
            for (var _k in cpm_duration){
                _s += _k + ':' + cpm_duration[_k] + ', ';
            }
            console.log(_s);

            var cpm1 = new CPM(cpm_duration);
            cpm1.run();
            nodes = cpm1.nodes;
            var $table = $tables[(j ? 0 : 1)];
            for(var k in nodes) {
                var $tr = $('td:contains('+k.replace('#', '')+')', $table).parent();
                if (nodes[k]['duration'] != old_nodes[k]['duration']) {
                    //console.log(k+' 趕工 '+(old_nodes[k]['duration']-nodes[k]['duration'])+' 天');
                    $('td:eq(1)', $tr).html((old_nodes[k]['duration'] - nodes[k]['duration'])).css('color', 'blue');
                }
                if (nodes[k]['tf'] != old_nodes[k]['tf']) {
                    console.log(k+' 浮時減少 ('+old_nodes[k]['tf']+' - '+nodes[k]['tf']+') 天');
                    $('td:eq(2)', $tr).html((old_nodes[k]['tf'] - nodes[k]['tf'])).css('color', 'blue');
                }
            }
        }


        var cost = 0;
        var result = '';
        for(var i=0; i<durations.length; i++){
            if (0 === cpm.nodes['#'+durations[i]]['tf']) {
                cost += c_prices['#'+durations[i]];
                result += make_line('要徑工項: #' + durations[i] + ', 成本： ' + c_prices['#'+durations[i]]);
            }
        }
        l = cost + ' * 0.4';
        cost = eval(l);
        result += make_line('總機具成本: ' + l + ' = ' + cost + ' 萬');
        l = cost + ' * ' + cpm.nodes['#End']['es'] + ' / 365';
        var depreciation = Math.round(eval(l) * 100) / 100;
        result += make_line('折舊費： ' + l + ' = ' + depreciation + ' 萬元(工期有 ' + cpm.nodes['#End']['es'] + ' 天)');
        $('#depreciation').html(result).css('color', 'blue');
    }
    function cal_bid_prices () {
        var l = '';
        var result = '';
        var $C_table = $('td:contains(請依序代貴企業的廠商代號第 3 及 6 碼，若為 0 ，請改代 1):first').parents('table');
        var $R_table = $('td:contains(請代貴企業的廠商代號第 5 碼，若為 0 ，請改代 1):first').parents('table');

        var l = '50 * ' + (contractor_number[2] ? contractor_number[2] : 1);
        var c11 = eval(l);
        $('tr:eq(1) td:eq(3)', $C_table).text(l+' = '+c11);
        var l = '400 * ' + (contractor_number[5] ? contractor_number[5] : 1);
        var c12 = eval(l);
        $('tr:eq(1) td:eq(4)', $C_table).text(l+' = '+c12);

        var l = '20 * ' + (contractor_number[2] ? contractor_number[2] : 1);
        var c21 = eval(l);
        $('tr:eq(2) td:eq(3)', $C_table).text(l+' = '+c21);
        var l = '200 * ' + (contractor_number[5] ? contractor_number[5] : 1);
        var c22 = eval(l);
        $('tr:eq(2) td:eq(4)', $C_table).text(l+' = '+c22);

        var l = '100 * ' + (contractor_number[2] ? contractor_number[2] : 1);
        var c31 = eval(l);
        $('tr:eq(3) td:eq(3)', $C_table).text(l+' = '+c31);
        var l = '300 * ' + (contractor_number[5] ? contractor_number[5] : 1);
        var c32 = eval(l);
        $('tr:eq(3) td:eq(4)', $C_table).text(l+' = '+c32);

        var l = '50 * ' + (contractor_number[4] ? contractor_number[4] : 1);
        var r1 = eval(l);
        $('tr:eq(1) td:eq(3)', $R_table).text(l+' = '+r1);

        var l = '20 * ' + (contractor_number[4] ? contractor_number[4] : 1);
        var r2 = eval(l);
        $('tr:eq(2) td:eq(3)', $R_table).text(l+' = '+r2);

        var l = '100 * ' + (contractor_number[4] ? contractor_number[4] : 1);
        var r3 = eval(l);
        $('tr:eq(3) td:eq(3)', $R_table).text(l+' = '+r3);

        var l = c11 + ' * ' + c12 + ' + ' + c21 + ' * ' + c22 + ' + ' + c31 + ' * ' + c32;
        l = '總價承包契約： ' + l + ' = '+ eval(l);
        result += make_line(l);

        var l = r1 + ' * ' + c12 + ' + ' + r2 + ' * ' + c22 + ' + ' + r3 + ' * ' + c32;
        l = '單價承包契約： ' + l + ' = '+ eval(l);
        result += make_line(l);

        var l = c11 + ' * ' + c12 + ' + ' + c21 + ' * ' + c22 + ' + ' + r3 + ' * ' + c32;
        l = '數量精算式總價承包契約： ' + l + ' = '+ eval(l);
        result += make_line(l);

        var l = '(' + r1 + ' * ' + c12 + ' + ' + r2 + ' * ' + c22 + ' + ' + r3 + ' * ' + c32 + ') * 1.03';
        l = '成本報酬契約： ' + l + ' = '+ eval(l);
        result += make_line(l);

        $('#bid_prices').html(result).css('color', 'blue');
    }
    function cal_guarantee_prices () {
        var l = '';
        var result = '';
        var data = [
            [2, 3, 0, 0, 0, '', '', ''],
            [2, 0, 0, 0, 0, '', '', ''],
            [1, 9, 3, 0, '', '', 1, ''],
            [1, 8, '', 8, 0, '', 1, ''],
            [1, '', 7, '', 7, '', 7, 1]
        ];
        for (var i=0; i<data.length; i++){
            data[i] = change_number(data[i], [2, 3, 4]);
        }
        var $table = $('td:contains(底價／標價)').parents('table');
        var i = 0;
        $table.find('tr:gt(0)').each(function(){
            var j = 0;
            $(this).find('td:gt(0)').each(function(){
                $(this).text(data[i][j]);
                j += 1;
            });
            i += 1;
        });

        var names = ['A廠商', 'B廠商', '貴企業'];
        var name = {};
        var cs = [];
        for (var i=2; i<data.length; i++){
            var value = list_to_number(data[i]);
            name[value] = names[i-2];
            if (cs.length > 0 && value < cs[0]) {
                cs.unshift(value);
            } else {
                cs.push(value);
            }
        }

        l = '得標廠商： ' + name[cs[0]];
        result += make_line(l);
        l = '得標金額： ' + cs[0];
        result += make_line(l);

        l = list_to_number(data[0]) + ' * 0.05';
        l = '押標金： ' + l + ' = '+ eval(l);
        result += make_line(l);

        l = list_to_number(data[0]) + ' * 0.1';
        var l1 = '履約保證金(預算＊0.1)： ' + l + ' = '+ eval(l);
        l = cs[0] + ' * 0.1';
        l1 += ' ，或是契約金額＊0.1： ' + l + ' = '+ eval(l) + ' 都可以，端視招標公告內容（但老師沒指定，所以都行）';
        result += make_line(l1);

        var l0 = '(' + cs[1] + ' + ' + cs[2] + ') / 2';
        if ( (cs[1] + cs[2])/2 * 0.8 > cs[0] ) {
            l = list_to_number(data[1]) + ' * 0.8 - ' + cs[0];
            l = '得標價在有效標平均標價('+l0+' = '+eval(l0)+')以下，須繳納差額保證金: ' + l + ' = ' + eval(l);
        } else {
            l = '得標價在有效標平均標價('+l0+' = '+eval(l0)+')以上，不須繳納差額保證金';
        }
        result += make_line(l);

        l = list_to_number(data[0]) + ' * 0.05';
        var l1 = '保固保證金(預算＊0.05)： ' + l + ' = '+ eval(l);
        l = cs[0] + ' * 0.05';
        l1 += ' ，或是契約金額＊0.05： ' + l + ' = '+ eval(l) + ' 都可以，端視招標公告內容（但老師沒指定，所以都行）';
        result += make_line(l1);

        $('#guarantee_prices').html(result).css('color', 'blue');
    }
    function cal_quality_control () {
        var result = '';
        var data = [
            [2, 5, 0],
            [2, 4, 9],
            [2, 2, 0],
            [2, 4, 5],
            [2, 3, 0],
            [2, 4, 5],
            [2, 4, 5],
            [2, 2, 2],
            [2, 3, 5],
            [2, 5, 6],
            [2, 4, ''],
            [2, 3, ''],
            [2, 3, ''],
            [2, 5, ''],
            [2, 5, ''],
            [2, 2, ''],
            [2, 1, ''],
            [2, 6, ''],
            [2, 3, ''],
            [2, 4, '']
        ];
        for (var i=0; i<10; i++) {
            data[i+10] = change_number(data[i+10], [i+1]);
        }
        var i = 10;
        $('td:contains(編號11~20)').parent().find('td:gt(0)').each(function(){
            $(this).text(list_to_number(data[i]));
            i += 1;
        });

        var avg_list = [];
        var r_list = [];
        var total = 0;
        var total_R = 0;
        for (var i=0; i<10; i++) {
            var v1 = list_to_number(data[i*2]);
            var v2 = list_to_number(data[i*2+1]);
            var avg = '(' + v1 + ' + ' + v2 + ')/2';
            var value = eval(avg);
            var l = 'Xbar_'+(i+1)+' = ' + avg + ' = ' + value;
            var r = 'Math.abs(' + v1 + ' - ' + v2 + ')';
            r_list.push(eval(r));
            var R = 'R_'+(i+1) + ' = ' + r + ' = ' + eval(r);
            result +=  make_line(l + '; ' + R);
            avg_list.push(value);
            total += value;
            total_R += eval(r);
        }
        l = 'Xbarbar(CL) = (' + avg_list.join(' + ') + ') / 10 = ' + (total / 10);
        result +=  make_line(l);

        l = (total / 10) + ' + ' + (total_R/10) + ' * 1.88';
        result +=  make_line('Xbar UCL = ' + l + ' = ' + eval(l));
        l = (total / 10) + ' - ' + (total_R/10) + ' * 1.88';
        result +=  make_line('Xbar LCL = ' + l + ' = ' + eval(l));

        l = 'Rbar(CL) = (' + r_list.join(' + ') + ') / 10 = ' + (total_R / 10);
        result +=  make_line(l);

        l = (total_R/10) + ' * 3.267';
        result +=  make_line('R UCL = ' + l + ' = ' + eval(l));
        result +=  make_line('R DCL = 無');

        $('#quality_control').html(result).css('color', 'blue');
    }
    function cal_rational_bid () {
        var l = '';
        var result = '';
        var data = [
            [2, '', '', '', '', '', '', ''],
            [2, '', '', '', '', '', '', ''],
            [2, '', '', '', '', '', '', ''],
            [1, '', 3, '', '', '', '', ''],
            [2, '', '', 4, '', '', '', ''],
            [2, '', '', '', 5, '', '', ''],
            [3, '', '', '', '', 6, '', ''],
            [2, '', '', '', '', '', 7, '']
        ];
        data[0] = change_number(data[0], [1, 2, 3, 4, 5, 6, 7]);
        data[1] = change_number(data[1], [2, 3, 4, 5, 6, 7, 8]);
        data[2] = change_number(data[2], [3, 4, 5, 6, 7, 8, 9]);
        var l = '('+list_to_number(data[0])+' + '+list_to_number(data[1])+' + '+list_to_number(data[2])+') / 3';
        var s1 = eval(l);
        var l = '機關底價： ' + l + ' = '+ s1;
        result += make_line(l);

        data[3] = change_number(data[3], [1, 2, 3, 4, 5, 6]);
        data[4] = change_number(data[4], [2, 3, 4, 5, 6, 7]);
        data[5] = change_number(data[5], [3, 4, 5, 6, 7, 8]);
        data[6] = change_number(data[6], [4, 5, 6, 7, 8, 9]);
        data[7] = change_number(data[7], [5, 6, 7, 8, 9, 10]);

        var names = ['A廠商', 'B廠商', 'C廠商', 'D廠商', '貴企業'];
        var name = {};
        var cs = [];
        var ls = [];
        var l = '廠商標價上下限: ' + (s1 * 0.8) + ' ~ ' + (s1*1.2);
        result += make_line(l);
        for (var i=3; i<data.length; i++) {
            var value = list_to_number(data[i]);
            if (s1*0.8 <= value && value <= s1*1.2) {
                name[value] = names[i-3];
                cs.push(value);
                ls.push(value);
            } else {
                ls.push(' 0 * ' + value);
            }
        }
        var l = '(' + ls.join(' + ') + ') / ' + cs.length;
        var s2 = eval(l);
        var l = '廠商平均標價： ' + l + ' = '+ s2;
        result += make_line(l);

        var final_bids = [];
        var l = s1 + ' * 0.7 + ' + s2 + ' * 0.3';
        var s = eval(l);
        result += make_line('開標底價: ' + l + ' = ' + s);
        for (var i=0; i<cs.length; i++) {
            if (s*0.9 <= cs[i] && cs[i] <= s) {
                if (final_bids.length > 0 && Math.abs(s - cs[i]) < Math.abs(s - final_bids[0])) {
                    final_bids.unshift(cs[i]);
                } else {
                    final_bids.push(cs[i]);
                }
            }
        }
        if (final_bids.length > 0) {
            var l = '得標廠商： ' + name[final_bids[0]];
            result += make_line(l);
            var l = '得標價格： ' + final_bids[0];
            result += make_line(l);
        } else {
            result += make_line('無人得標');
        }

        $('#rational_bid').html(result).css('color', 'blue');

        var i = 0;
        $('td:contains(審計機關)').parents('table').find('tr').each(function(){
            if (i > 0) {
                var j = 0;
                $(this).find('td:gt(0)').each(function(){
                    $(this).text(data[i-1][j]);
                    j += 1;
                });
            }
            i += 1;
        })

        var i = 0;
        $('td:contains(D廠商)').parents('table').find('tr').each(function(){
            if (i > 0) {
                var j = 0;
                $(this).find('td:gt(0)').each(function(){
                    $(this).text(data[i+2][j]);
                    j += 1;
                });
            }
            i += 1;
        })
    }
    $(document).ready(function(){
        $('#calculate').click(calculate);
        $('#calculate').click();
    });
})(jQuery);

