---
layout: page
---

<div class="row">
    <div class="col-sm-3"><img src="{{ site.baseurl }}public/mug18.png" alt="Photo of Trevor"></div> 
    <div class="col-sm-9">
	  <div class="row">
	    <div class="col-sm-5">
	      <b>Trevor Cohn</b>
	      <br>Professor 
              <br>Research Scientist, Google Research Australia
	      <address>
		Level 4, Melbourne Connect 
	      </address>
	    </div>
		<div class="col-sm-5">
		  <a href="http://www.cis.unimelb.edu.au">Computing and Information Systems</a><br/>
		  <a href="http://www.unimelb.edu.au">The University of Melbourne</a><br/>
		  <a href="https://cis.unimelb.edu.au/research/artificial-intelligence/research/Natural-Language-Processing">Natural Language Processing group</a>
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
  human language, with several applications including automatic translation.
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

{% include publications.html year=2024 %}
{% include publications.html year=2023 %}
