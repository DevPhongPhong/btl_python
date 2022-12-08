$.ajax({
    url: '/api/post/get-five-post-highest-viewcount',
    type: 'GET',
    success: function (data) {
        const btl_most_view = document.getElementById('btl_most_view')
        btl_most_view.innerHTML = `<div class="col-12">
                                    <div class="product-box-layout1">
                                        <figure class="item-figure"><a href="/post/${data[0].id[0]}"><img
                                                    src="${data[0].main_image[0]}" alt="Post"></a></figure>
                                        <div class="item-content">
                                            <span class="sub-title">${data[0].category[0].toUpperCase()}</span>
                                            <h2 class="item-title"><a href="/post/${data[0].id[0]}">${data[0].title[0]}</a></h2>
                                            <p>${data[0].sub_content[0]}.. </p>
                                            <p>${data[0].sub_content[0]}</p>
                                            <ul class="entry-meta">
                                                <li><a href="#"><i class="fas fa-clock"></i>${data[0].created_time[0]}</a></li>
                                                <li><a href="#"><i class="fas fa-user"></i>by <span>${data[0].author[0]}</span></a></li>

                                            </ul>
                                        </div>
                                    </div>
                                </div>`
        for (i = 1; i < data.length; i++) {
            btl_most_view.innerHTML += `  <div class="col-md-6 col-sm-6 col-12">
                                                <div class="product-box-layout1">
                                                    <figure class="item-figure"><a href="/post/${data[i].id[0]}"><img
                                                                src="${data[i].main_image[0]}"  alt="Post"></a></figure>
                                                    <div class="item-content">
                                                        <span class="sub-title">${data[i].category[0].toUpperCase()}</span>
                                                        <h3 class="item-title"><a href="/post/${data[i].id[0]}">${data[i].title[0]}</a></h3>
                                                        <p>${data[i].sub_content[0]}.. </p>
                                                        <ul class="entry-meta">
                                                            <li><a href="#"><i class="fas fa-clock"></i>${data[i].created_time[0]}</a></li>
                                                            <li><a href="#"><i class="fas fa-user"></i>by <span>${data[1].author[0]}</span></a></li>

                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>`
        }
    }
})

