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
                                            <h2 class="item-title"><a href="/post/${data[0].id[0]}">${data[i].title[0]}</a></h2>
                                            <p>${data[i].sub_content[0]}.. </p>
                                            <p>${data[0].sub_content[0]}</p>
                                            <ul class="entry-meta">
                                                <li><a href="#"><i class="fas fa-clock"></i>${data[0].created_time[0]}</a></li>
                                                <li><a href="#"><i class="fas fa-user"></i>by <span>${data[0].author[0]}</span></a></li>

                                            </ul>
                                        </div>
                                    </div>
                                </div>`
        for (i = 1; i < 5; i++) {
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


var btl_most_view = document.getElementById('btl_most_view')
btl_most_view.innerHTML = ` <div class="col-md-6 col-sm-6 col-12">
                                <div class="product-box-layout1">
                                    <figure class="item-figure"><a href="single-recipe1.html"><img
                                                src="/static/img/product/product10.jpg"  alt="Post"></a></figure>
                                    <div class="item-content">
                                        <span class="sub-title">GÀ</span>
                                        <h3 class="item-title"><a href="single-recipe1.html">Mỳ gà Châu Á</a></h3>

                                        <p>img/product/product10.jpg</p>
                                        <ul class="entry-meta">
                                            <li><a href="#"><i class="fas fa-clock"></i>54 phút trước</a></li>
                                            <li><a href="#"><i class="fas fa-user"></i>by <span>Nguyễn Hải
                                                        Phong</span></a></li>

                                        </ul>
                                    </div>
                                </div>
                            </div>
                                <div class="col-md-6 col-sm-6 col-12">
                                <div class="product-box-layout1">
                                    <figure class="item-figure"><a href="single-recipe1.html"><img
                                                src="/static/img/product/product6.jpg"  alt="Post"></a></figure>
                                    <div class="item-content">
                                        <span class="sub-title">SALAD</span>
                                        <h3 class="item-title"><a href="single-recipe1.html">Salad trộn Italy</a></h3>

                                        <p>Món salad kiểu Ý này có vị giòn ngọt của rau xà lách, vị bùi bùi beo béo của
                                            phô mai và trứng, ăn vào thì mát cả ruột, chắc chắn sẽ là một món rất thích
                                            hợp cho những ngày hè oi ả như thế này. </p>
                                        <ul class="entry-meta">
                                            <li><a href="#"><i class="fas fa-clock"></i>30 phút trước</a></li>
                                            <li><a href="#"><i class="fas fa-user"></i>by <span>Nguyễn Hải
                                                        Phong</span></a></li>

                                        </ul>
                                    </div>
                                </div>
                                </div>
                                <div class="col-md-6 col-sm-6 col-12">
                                <div class="product-box-layout1">
                                    <figure class="item-figure"><a href="single-recipe1.html"><img
                                                src="/static/img/product/product7.jpg"  alt="Post"></a></figure>
                                    <div class="item-content">
                                        <span class="sub-title">BỮA TỐI</span>
                                        <h3 class="item-title"><a href="single-recipe1.html">Món tráng miệng Mexico</a>
                                        </h3>

                                        <p>Trong tiếng Tây Ban Nha, trứng tráng đôi khi được gọi là "tortilla de huevos"
                                            có nghĩa là "tortilla trứng". Đây là một trong những thành phần phong cách
                                            Mexico và làm cho một bữa ăn sáng ngon.</p>
                                        <ul class="entry-meta">
                                            <li><a href="#"><i class="fas fa-clock"></i>15 phút trước</a></li>
                                            <li><a href="#"><i class="fas fa-user"></i>by <span>Nguyễn Hải
                                                        Phong</span></a></li>

                                        </ul>
                                    </div>
                                </div>
                                </div>
                                <div class="col-md-6 col-sm-6 col-12">
                                <div class="product-box-layout1">
                                    <figure class="item-figure"><a href="single-recipe1.html"><img
                                                src="/static/img/product/product8.jpg"  alt="Post"></a></figure>
                                    <div class="item-content">
                                        <span class="sub-title">NƯỚC</span>
                                        <h3 class="item-title"><a href="single-recipe1.html">Nước đậu nành</a></h3>

                                        <p>Sữa đậu nành là một thức uống mang lại giá trị dinh dưỡng khá cao cho cơ thể,
                                            nó cũng là một thức uống thơm ngon được rất nhiều người yêu thích.</p>
                                        <ul class="entry-meta">
                                            <li><a href="#"><i class="fas fa-clock"></i>39 phút trước</a></li>
                                            <li><a href="#"><i class="fas fa-user"></i>by <span>Nguyễn Hải
                                                        Phong</span></a></li>
                                        </ul>
                                    </div>
                                </div>
                                </div>`