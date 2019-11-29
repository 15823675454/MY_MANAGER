// 所有学生
function all_student() {
    var token = window.localStorage.getItem('manager_token');
    //登陆的用户名
    var username = window.localStorage.getItem('manager_user')
    var post_data = { 'username': username.toString() }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/all_student',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                // console.log(result)
                left_html = ''
                // 班级
                $.each(result.class_list, function (index, element) {
                    // console.log(element)
                    left_html += '<a href="#" onclick="get_one_class_info(this.id)" id="'
                    left_html += element
                    left_html += '">'
                    left_html += element
                    left_html += '</a>'
                })
                $('#class_manager').html(left_html)
                html = '<figure><table id="tb"><thead><tr><th><span>序号</span></th><th><span>姓名</span></th><th><span>学号</span></th><th><span>班级</span></th><th><span>美术成绩</span></th><th><span>操作</span></th></tr></thead><tbody id="content"></tbody></table</figure>'
                // 具体学生
                $.each(result.data, function (index, element) {
                    html += '<tr><td>' + (index + 1) + '</td><td  class="name_color">' + element.name + '</td><td>' + element.stu_id + '</td><td>' + element.stu_class + '</td><td>' + element.score + '</td>'
                    html += '<td><span class="c_student" onclick="stu_info(this.id)" id="'
                    html += element.stu_id
                    html += '">修改</span>|<span class="c_student" onclick="del_stu(this.id)" id="'
                    html += element.name + '&' + element.stu_id
                    html += '">删除</span>'
                    html += '</tr>'
                })
                html += '<button onclick="print_student()">打印</button>'
                $('#write').html(html)
            }
            else {
                alert(result.error)
                console.log(result.error)
            }
        }
    })
}

// 退出
function logout() {
    if (confirm("确定登出吗？")) {
        window.localStorage.removeItem('manager_token');
        window.localStorage.removeItem('manager_user');
        window.localStorage.removeItem('all_class');
        window.localStorage.removeItem('all_stu_art');
        window.location.href = '/';
    }
}
// 获取单个班级信息
function get_one_class_info(myid) {
    var teacher = window.localStorage.getItem('manager_user')
    var token = window.localStorage.getItem('manager_token')
    var post_data = { 'teacher': teacher }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/one_class/' + myid,
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                html = '<figure><table id="tb"><thead><tr><th><span>序号</span></th><th><span>姓名</span></th><th><span>学号</span></th><th><span>班级</span></th><th><span>美术成绩</span></th></tr></thead><tbody id="content"></tbody></table</figure>'
                $.each(result.data, function (index, element) {
                    html += '<tr><td>' + (index + 1) + '</td><td onclick="stu_info(this.id)" class="name_color" id="'+element.stu_id + '">' + element.name + '</td><td>' + element.stu_id + '</td><td>' + element.stu_class + '</td><td>' + element.score + '</td></tr>'
                })
                $('#write').html(html)
            }

        }
    })
}
// 学生信息获取(未完成)
function stu_info(stu_id){
    // console.log(stu_id)
    var token = window.localStorage.getItem('manager_token')
    var post_data = { 'student': stu_id }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/student/' + stu_id,
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                console.log(result)
            }

        }
    })
}
// 所有学生作品
function stu_art(){
    var token = window.localStorage.getItem('manager_token')
    var teacher = window.localStorage.getItem('manager_user')
    var post_data = { 'teacher': teacher }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/student',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                // 遍历学生列表,获取到单个学生
                html = ''
                $.each(result.data, function(index, element){
                    var stu_name = element.name
                    // console.log(stu_name)
                    // 遍历单个学生所有作品
                    $.each(element.art, function(index_i, element_i){
                        html += '<div class="c_img">'
                        html += '<img class="stu_img" src="http://176.221.13.63:8000/media/'
                        html += element_i.img
                        html += '">'
                        html += '<span class="t">'
                        html += stu_name  
                        html += '&nbsp;|&nbsp;'
                        html += element_i.score
                        html += '</span>'
                        html += '</div>'
                        // console.log(html)
                    })
                })
                $('#write').html(html)
                window.localStorage.setItem('all_stu_art', JSON.stringify(result.data))
            }

        }
    })
}
// 加载添加学生界面
function add_student_html(){
    $('#write').load('/add#student')
}
// 添加学生
function add_student(){
    var name = $('#student_name').val()
    var stu_id = $('#stu_id').val()
    var stu_class = $('#stu_class').val()
    var gender = $("input:radio[name='gender']:checked").val()
    var age = $('#age').val()
    var appraise = $('#appraise').val()
    var avatar = $('#avatar').val()
    var phone = $('#phone').val()
    var address = $('#address').val()
    var teacher = window.localStorage.getItem('manager_user')
    var token = window.localStorage.getItem('manager_token')
    var post_data = {'name': name,'stu_id':stu_id,'stu_class':stu_class,'gender':gender,'age':age,'appraise':appraise,'avatar':avatar,'phone':phone, 'teacher': teacher, 'address':address}
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/student/add',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                $('#show').html('添加学生'+name+'成功')
            }
            else if(result.code == 601){
                alert('该教师已不存在!请登录')
                window.location.href = '/'
            }
            else{
                alert(result.error)
            }

        }
    })
}
// 加载所有班级界面
function student_file(){
    $('#write').load('/interior/student/class#tabs')
}
// 加载作品界面
function load_art(){
    $('#write').load('/art#tabs')
}
// 修改学生信息(待完成)
function up_stu(t_id){

}
// 删除学生信息
function del_stu(t_id){
    var teacher = window.localStorage.getItem('manager_user')
    var token = window.localStorage.getItem('manager_token')
    var post_data = { 'teacher': teacher }
    $.ajax({
        url: 'http://176.221.13.63:8000/delete/' + t_id,
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                alert('删除学生'+result.name + '成功')
                show_class()
                student_file()
                return
            }
            else if (result.code == 102 || result.code == 803)
                alert(result.error)
                window.location = '/'
        }
    })
}
// 班级学生
function show_class(){
    var token = window.localStorage.getItem('manager_token');
    //登陆的用户名
    var username = window.localStorage.getItem('manager_user')
    var post_data = { 'username': username.toString() }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/all_student',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                window.localStorage.setItem('all_class', JSON.stringify(result.data))
                // console.log(result)
                class_html = ''
                // 班级
                $.each(result.class_list, function (index, element) {
                    // <li><a href="#" title="table_d">一班  </a></li>
                    class_html += '<li><a title="table_d" onclick="stu_class(this.id)" id="'
                    class_html += element
                    class_html += '">'
                    class_html += element 
                    class_html += '</a></li>'
                })
                $('#tabs').html(class_html)
                
            }
            else {
                alert(data.error)
            }
        }
    })
  }

// 加载修改教师基本信息页面
function tec_setting_html(){
    $('#write').load('/setting #set')
}


// 教师基本信息设置
function tec_setting(){
    var token = window.localStorage.getItem('manager_token');
    //登陆的用户名
    var username = window.localStorage.getItem('manager_user')
    var post_data = { 'username': username }
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/teacher',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                window.localStorage.setItem('all_class', JSON.stringify(result.data))
                // console.log(result)
                class_html = ''
                // 班级
                $.each(result.class_list, function (index, element) {
                    // <li><a href="#" title="table_d">一班  </a></li>
                    class_html += '<li><a title="table_d" onclick="stu_class(this.id)" id="'
                    class_html += element
                    class_html += '">'
                    class_html += element 
                    class_html += '</a></li>'
                })
                $('#tabs').html(class_html)
                
            }
            else {
                alert(data.error)
            }
        }
    })
}


// 打印学生(待完成)
function print_student(){
    var token = window.localStorage.getItem('manager_token')
    var user = window.localStorage.getItem('manager_user')
    var post_data = {'token': token, 'user': user}
    $.ajax({
        url: 'http://176.221.13.63:8000/interior/print_student',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        // success: function (result) {
        //     console.log(6666666666666666)
        //     alert('打印成功')
        // }
    })
}








