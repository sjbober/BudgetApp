// Adding the proper URL's to each pagination link and determining which page is active to add the correct class -->

window.addEventListener("load", addActiveClass);
window.addEventListener("load", addURLs);

function addActiveClass() {
  let pageLinks = document.getElementsByClassName("page-num");

  if ( page_number == "None" ) {
    pageLinks[0].className = "page-item active" ;
  } else {
    for (let i = 0; i < pageLinks.length; i++) {
          if ( page_number == pageLinks[i].innerText ) {
            pageLinks[i].className = "page-item active" ;
            break;
          }
        }
  }
}

function addURLs() {
  let pageLinks = document.getElementsByClassName("page-num");

  for (let i = 0; i < pageLinks.length; i++) {
    let page_number = pageLinks[i].innerText;
    pageLinks[i].childNodes[0].href = "?page=" + page_number;
  }
}

{/* 
  
<nav aria-label="..." class="flex just-center">
<ul class="pagination">

{% if page_obj.has_previous %}
  <li class="page-item">
    <a class="page-link" href="?page={{ page_obj.previous_page_number }}"><i class="fas fa-angle-left"></i> Previous</a>
  </li>
{% else %}
  <li class="page-item disabled">
    <span class="page-link"><i class="fas fa-angle-left"></i> Previous</span>
  </li>
{% endif %}


{% for page_num in page_range %}

  <li class="page-item page-num"><a class="page-link" href="">{{ page_num }}</a></li>

{% endfor %}


  {% if page_obj.has_next %}
  <li class="page-item">
    <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next <i class="fas fa-angle-right"></i></a>
  </li>
  {% else %}
  <li class="page-item disabled">
    <span class="page-link ">Next <i class="fas fa-angle-right"></i></span>
  </li>
  {% endif %}


  </li>
</ul>
</nav> 

*/}