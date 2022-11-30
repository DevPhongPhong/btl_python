setAuth=(name)=>{
    var loginShow = document.getElementById('btl_loginShow');
    loginShow.innerHTML = `<button type="button" class="login-btn" onclick="LogOut()">
                                <i class="flaticon-profile"></i>Đăng xuất
                            </button>`
}

LogOut =() =>{
    alert('logout')
}

$.ajax({
    url:'/api/post/get-five-post-highest-viewcount',
    type:'GET',
    success: function (res){
        console.log(res)
    }
})
