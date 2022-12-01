$.ajax({
    url:'/api/post',
    success: (res)=>{
        btl_postbody = document.getElementById('btl_postbody')
        btl_postbody.innerHTML = ''
        for(i=0;i<res.length;i++){
            btl_postbody.innerHTML+=`<tr>
                                        <td>${res[i].id[0]}</td>
                                        <td>${res[i].title}</td>
                                        <td>${res[i].sub_content[0]}</td>
                                        <td>${res[i].viewcount[0]}</td>
                                        <td>${res[i].created_time[0]}</td>
                                        <td>${res[i].category[0]}</td>
                                        <td>
                                        <button onclick="deletePost(${res[i].id[0]})">Xóa</button>
                                        <a href="/admin/changepost/${res[i].id[0]}">Sửa</button>
                                        <a href="/post/${res[i].id[0]}">Xem</a>
                                        </td>
                                    </tr>`
        }
        
    }
})
$.ajax({
    url:'/api/category',
    success: (res)=>{
        btl_catebody = document.getElementById('btl_catebody')
        btl_catebody.innerHTML = ''
        for(i=0;i<res.length;i++){
            btl_catebody.innerHTML+=`<tr>
                                        <td>${res[i].id[0]}</td>
                                        <td>${res[i].name[0]}</td>
                                        <td>${res[i].main_image[0]}</td>
                                        <td>
                                            <button onclick="deleteCate(${res[i].id[0]})">Xóa</button>
                                            <a href="/admin/changecategory/${res[i].id[0]}">Sửa</button>
                                            <a href="/category/${res[i].id[0]}">Xem</a>
                                        </td>
                                    </tr>`
        }
        
    }
})

deletePost=(id)=>{
    $.ajax({
        url:`/api/post/delete/${id}`,
        type:'DELETE',
        success: (res)=>{
            location.reload();
        }
    })
}

deleteCate=(id)=>{
    $.ajax({
        url:`/api/category/delete/${id}`,
        type:'DELETE',
        success: (res)=>{
            location.reload();
        }
    })
}