$.ajax({
    url: '/api/post/get-three-post-random',
    type: 'GET',
    success: function (data) {
        const btl_random_post = document.getElementById('btl_random_post')
        btl_random_post.innerHTML=''
        for(i=0;i<3;i++){
            btl_random_post.innerHTML += `  <div class="col-lg-4 col-md-6 col-sm-12">
                                                <div class="product-box-layout1">
                                                    <figure class="item-figure"><a href="/post/${data[i].id[0]}"><img
                                                                src="${data[i].main_image[0]}"  alt="Post"></a></figure>
                                                    <div class="item-content">
                                                        <span class="sub-title">${data[i].category[0].toUpperCase()}</span>
                                                        <h3 class="item-title"><a href="/post/${data[i].id[0]}">${data[i].title[0]}</a></h3>
                                                        <p>${data[i].sub_content[0]}.. </p>
                                                        <ul class="entry-meta">
                                                            <li><a href="#"><i class="fas fa-clock"></i>${data[i].created_time[0]}</a></li>
                                                            <li><a href="#"><i class="fas fa-user"></i>by <span>${data[i].author[0]}</span></a></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>`
        }
    }
})