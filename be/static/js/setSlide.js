$.ajax({
    url: '/api/post/get-three-post-latest',
    type: 'GET',
    success: function (data) {
        const btl_slide = document.getElementById("btl_slide");
        btl_slide.innerHTML = ''
        for (i = 0; i < 3; i++) {
            btl_slide.innerHTML += `<div class="ranna-slider-content-layout1">
                                        <figure class="item-figure"><a href="/post/${data[i].id[0]}"><img src="${data[i].main_image[0]}" style="max-height: 545.99px;"
                                                    alt="slide-${i}"></a></figure>
                                        <div class="item-content">
                                            <span class="sub-title">${data[i].category[0].toUpperCase()}</span>
                                            <h2 class="item-title"><a href="/post/${data[i].id[0]}">${data[i].title[0]}</a></h2>
                                            <p>${data[i].sub_content[0]}.. </p>
                                            <ul class="entry-meta">
                                                <li><a href="#"><i class="fas fa-clock"></i>${data[i].created_time[0]}</a></li>
                                                <li><a href="#"><i class="fas fa-user"></i>by <span>${data[i].author[0]}</span></a></li>
                                            </ul>
                                        </div>
                                    </div>`
        }
    }
})


