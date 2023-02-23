# 0x01. AirBnB clone - Web static
## Project Description 
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:
+ Create simple HTML static pages
+ Style guide
+ Fake contents
+ No Javascript
+ No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.
## Notes 
Emails often include HTML content. When you receive a fancy looking e-mail, it is either one big image file or it is an HTML e-mail. You can craft HTML e-mails yourself, but they can be tricky. The HTML viewers in email clients are not standardized, and most of them do not allow <style> tags. For this reason, HTML e-mail often contain lots of inline styles.

CSS cascades from top to bottom.  

Semantics within HTML is the practice of giving content on the page meaning and structure by using the proper element. Semantic code describes the value of content on a page, regardless of the style or appearance of that content.  

```htm
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Meta tag is very important -->
    <!-- Define the character set used -->
    <meta charset="utf-8">
    <!-- Define keywords for search engines-->
    <meta name="keywords" content="HTML, CSS, JavaScript">
    <!-- Define a description of your web page -->
    <meta name="description" content="Free Web tutorials">
    <!-- Define the author of a page: -->
    <meta name="author" content="John Doe">
    <!-- set viewport  -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```
Divisions, or <div>s, and <span>s are HTML elements that act as containers solely for styling purposes. As generic containers, they do not come with any overarching meaning or semantic value. Paragraphs are semantic in that content wrapped within a <p> element is known and understood as a paragraph. <div>s and <span>s do not hold any such meaning and are simply containers.

Both <div>s and <span>s, however, are extremely valuable when building a website in that they give us the ability to apply targeted styles to a contained set of content.

A <div> is a block-level element that is commonly used to identify large groupings of content, and which helps to build a web page’s layout and design. A <span>, on the other hand, is an inline-level element commonly used to identify smaller groupings of text within a block-level element.  
### Comments
HTML comments start with <!-- and end with -->. CSS comments start with /* and end with */.  

The <strong> element is semantically used to give strong importance to text, and is thus the most popular option for bolding text. The <b> element, on the other hand, semantically means to stylistically offset text, which isn’t always the best choice for text deserving prominent attention. We have to gauge the significance of the text we wish to set as bold and to choose an element accordingly.  

```htm
<!-- Strong importance -->
<p><strong>Caution:</strong> Falling rocks.</p>

<!-- Stylistically offset -->
<p>This recipe calls for <b>bacon</b> and <b>baconnaise</b>.</p>
```
For the longest time the structure of a web page was built using divisions. The problem was that divisions provide no semantic value, and it was fairly difficult to determine the intention of these divisions. Fortunately HTML5 introduced new [structurally based elements](https://dev.opera.com/articles/new-structural-elements-in-html5/), including the <header>, <nav>, <article>, <section>, <aside>, and <footer> elements.

The <header> element is a structural element that outlines the heading of a segment of a page. It falls within the <body> element.

The <head> element is not displayed on a page and is used to outline metadata, including the document title, and links to external files. It falls directly within the <html> element.  

## Links
+ [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/building-your-first-web-page/)  
+ [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)  
+ [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)  
+ [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
+ [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
+ [MozillaDevelopersNetwork?](https://developer.mozilla.org/en-US/)  
+ [CenterBoxes](https://css-tricks.com/centering-css-complete-guide/)  
+ [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/index.html)  
+ [A Dao of Web Design](http://alistapart.com/article/dao/)
+ [CSS Tools: Reset CSS](https://meyerweb.com/eric/tools/css/reset/)  
+ [Semantic code: What? Why? How?](https://boagworld.com/dev/semantic-code-what-why-how/)  