setAuth=(name)=>{
    var loginShow = document.getElementById('btl_loginShow');
    loginShow.innerHTML = `<button type="button" class="login-btn" onclick="LogOut()">
                                <i class="flaticon-profile"></i>Đăng xuất
                            </button>`
}

LogOut =() =>{
    alert('logout')
}

testCallAjax = ()=>{
    $.ajax({
        url:'http://127.0.0.1:5000/api/category/add',
        type:'POST',
        data:{"data1":"Hello"},
        dataType: 'json',
        success:function(res){
            alert('success');
        }
    });
}