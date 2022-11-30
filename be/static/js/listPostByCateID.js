currentPathname = window.location.pathname
btl_ListPost = document.getElementById('btl_ListPost')
btl_pagin = document.getElementById('btl_pagin')
allData = []
if (currentPathname.length == 5) {
    $.ajax({
        url: '/api/post',
        type: 'GET',
        success: function (res) {
            allData = res
            bindData(1, res)

        }
    })
}
else {
    id = currentPathname.substring(10, currentPathname.length)
    $.ajax({
        url: `/api/category/${id}`,
        type: 'GET',
        success: function (res) {
            btl_nameSection = document.getElementById('btl_nameSection')
            btl_nameSection.innerHTML+=` - Danh mục: ${res.name[0]}`
        }
    });

    $.ajax({
        url: `/api/post/category/${id}`,
        type: 'GET',
        success: function (res) {
            allData = res
            bindData(1, res)
        }
    })
}

bindData = (page, data) => {
    btl_ListPost.innerHTML = ''
    for (i = (page - 1) * 4; i < page * 4 && i < data.length; i++) {
        btl_ListPost.innerHTML += ` <div class="col-sm-6 col-12">
                                        <div class="blog-box-layout1">
                                            <div class="item-figure">
                                                <a href="/post/${data[i].id[0]}"><img src="${data[i].main_image[0]}" alt="Blog"></a>
                                            </div>
                                            <div class="item-content">
                                                <ul class="entry-meta">
                                                    <li><a href="#"><i class="fas fa-clock"></i>${data[i].created_time[0]}</a></li>
                                                    <li><a href="#"><i class="fas fa-user"></i>by <span>${data[i].author[0]}</span></a></li>
                                                </ul>
                                                <h3 class="item-title"><a href="/post/${data[i].id[0]}">${data[i].title}</a></h3>
                                                <p>${data[i].sub_content[0]}
                                                </p>
                                                <a href="/post/${data[i].id[0]}" class="item-btn">Đọc tiếp<i class="flaticon-next"></i></a>
                                            </div>
                                        </div>
                                    </div>`
    }
    btl_pagin.innerHTML = ''
    for (i = 1; i <= (data.length % 4 == 0 ? data.length / 4 : data.length / 4 + 1); i++) {
        btl_pagin.innerHTML += (i == page ? `<li class="btl_pagin active">
                                                <a href="#" onclick="bindData(${i},allData)">${i}</a>
                                            </li>`
                                            :
                                            `<li class="btl_pagin">
                                                <a href="#" onclick="bindData(${i},allData)">${i}</a>
                                            </li>`)
    }
}


