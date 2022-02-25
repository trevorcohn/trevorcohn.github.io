---
layout: page
---

<div class="row">
    <div class="col-sm-3"><img src="{{ site.baseurl }}public/mug18.png" alt="Photo of Trevor"></div> 
    <div class="col-sm-9">
	  <div class="row">
	    <div class="col-sm-3">
	      <b>Trevor Cohn</b>
	      <br>Professor 
	      <address>
		Room 323<br/>
		Doug McDonnell Building (#167)
	      </address>
	    </div>
		<div class="col-sm-7">
		  <a href="http://www.cis.unimelb.edu.au">Computing and Information Systems</a><br/>
		  <a href="http://www.unimelb.edu.au">The University of Melbourne</a><br/>
		  <a href="http://uom-nlp.github.io/">Natural Language Processing group</a>
		</div>
	  </div>
	  <div class="row">
	    <div class="col-sm-3">
	<script type="text/javascript"><!--
	document.write('<a href="' +
	'&#109;&#097;&#105;&#108;&#116;&#111;&#058;&#116;' +
	'&#099;&#111;&#104;&#110;&#064;&#117;&#110;&#105;' +
	'&#109;&#101;&#108;&#098;&#046;&#101;&#100;&#117;' +
	'&#046;&#097;&#117;&#013;&#010;">' +
	'<span class="glyphicon glyphicon-envelope"></span></a> Email');
	//-->
	</script>
	<noscript><IMG alt="E-mail" border=0 src="./email.jpg"></noscript>
	    </div>
	    <div class="col-sm-7"> Ph: +61383441732 </div>
	    </div>
	</div>
    </div>

<p class="message">
  Understanding of human language by computers has been a central goal of
  Artificial Intelligence since its beginnings, with massive potential to
  improve communication, provide better information access and automate basic
  human tasks. My research focuses on technologies for automatic processing of
  human language, with several applications including automatic translation 
  (akin to <a href="http://translate.google.com">Google</a> and
  <a href="http://www.bing.com/translator">Bing's</a> translation tools). 
  My core focus is on probabilistic machine learning modelling
  of language applications, particularly handling uncertain
  or partly observed data and structured prediction problems.
</p>

<h3>News</h3>
<ul>
{% for item in site.data.news.posts %}
  <li><i>{{ item.date }}</i>: {{ item.text }}</li>
{% endfor %}
</ul>

<h3>Recent Papers</h3>

{% include publications.html year=2022 %}
{% include publications.html year=2021 %}
