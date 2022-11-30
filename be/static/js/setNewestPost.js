$.ajax({
    url: '/api/post/get-three-post-latest',
    type: 'GET',
    success: function (data) {
        const btl_newestPost = document.getElementById("btl_newestPost");
        btl_newestPost.innerHTML = ''
        for (i = 0; i < 3; i++) {
            btl_newestPost.innerHTML += `<li class="single-item">
                                        <div class="item-img">
                                            <a href="/post/${data[i].id[0]}"><img src="${data[i].main_image[0]}" alt="Post" style="max-inline-size: 150px;"></a>
                                        </div>
                                        <div class="item-content">
                                            <div class="item-post-date"><a href="#"><i class="fas fa-clock"></i>${data[i].created_time[0]}</a></div>
                                            <h4 class="item-title"><a href="/post/${data[i].id[0]}">${data[i].title[0]}</a></h4>
                                            <div class="item-post-by"><a href="single-blog./post/${data[i].id[0]}"><i class="fas fa-user"></i><span>by</span>
                                            ${data[i].author[0]}</a></div>
                                        </div>
                                    </li>
                                    `
        }
    }
})


