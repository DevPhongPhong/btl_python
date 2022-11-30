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
