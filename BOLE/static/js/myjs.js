// 所有学生
function all_student() {
    var token = window.localStorage.getItem('manager_token');
    //登陆的用户名
    var username = window.localStorage.getItem('manager_user')
    var post_data = { 'username': username.toString() }
    $.ajax({
        url: 'http://127.0.0.1:8000/interior/all_student',
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                console.log(result)
                left_html = ''
                // 班级
                $.each(result.class_list, function (index, element) {
                    // console.log(element)
                    left_html += '<div class="open d_background">'
                    left_html += '<h3><span onclick="get_one_class_info(this.id)" id="'
                    left_html += element
                    left_html += '">'
                    left_html += element
                    left_html += '</span></h3></div>'
                })
                $('#my_class').html(left_html)
                html = ''
                // 具体学生
                $.each(result.data, function (index, element) {
                    html += '<tr><td>' + (index + 1) + '</td><td onclick="stu_info(this.id)" class="name_color" id="'+element.stu_id + '">' + element.name + '</td><td>' + element.stu_id + '</td><td>' + element.stu_class + '</td><td>' + element.score + '</td></tr>'
                })
                $('#content').html(html)
            }
            else {

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
        window.location.href = '/';
    }
}
// 获取单个班级信息
function get_one_class_info(myid) {
    var teacher = window.localStorage.getItem('manager_user')
    var token = window.localStorage.getItem('manager_token')
    var post_data = { 'teacher': teacher }
    $.ajax({
        url: 'http://127.0.0.1:8000/interior/one_class/' + myid,
        type: 'post',
        data: JSON.stringify(post_data),
        dataType: 'json',
        beforeSend: function (request) {
            request.setRequestHeader("Authorization", token);
        },
        success: function (result) {
            if (result.code == 200) {
                html = ''
                $.each(result.data, function (index, element) {
                    html += '<tr><td>' + (index + 1) + '</td><td onclick="stu_info(this.id)" class="name_color" id="'+element.stu_id + '">' + element.name + '</td><td>' + element.stu_id + '</td><td>' + element.stu_class + '</td><td>' + element.score + '</td></tr>'
                })
                $('#content').html(html)
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
        url: 'http://127.0.0.1:8000/interior/student/' + stu_id,
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
        url: 'http://127.0.0.1:8000/interior/student',
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


