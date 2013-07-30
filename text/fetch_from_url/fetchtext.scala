import scala.util.matching.Regex

object FetchText {

    def applyTemplate(t : String, g: Map[String, String]) =
        g.foldLeft(t) ((s, g1) => s.replace("{" + g1._1 + "}", g1._2))

    def parse(s : String, r: Regex, g: List[Int]) =
        (r findAllIn s).matchData map (m => (g map (g1 => (g1.toString -> m.subgroups(g1)))) toMap)

    def getGroups(t: String) =
        (("""\{(\d*?)\}""".r findAllIn t).matchData.toList map (s => s.subgroups(0).toInt))

    def fetchText(u : String, e : String, r : Regex, t: String) =
        parse(io.Source.fromURL(u, e).mkString, r, getGroups(t)).foldLeft("") ((s, m) => s + applyTemplate (t, m))
    
    def main(args: Array[String]) {
        val regex = "(?ism)\"item_name\">.*?<h2>(.*?)</h2>.*?item_right\">(.*?)</div.*?item_right\">(.*?)</div".r
        val template = "{0}{1}{2}\n"

        val subUrls = List("email", "url", "addresses", "datetime", "markup", "other", "strings", "phones", "numbers")
        val url = "http://regexp.com.ua/category/"
        val enc = "UTF-8"

        println ("taken from http://regexp.com.ua")
        
        subUrls foreach (s => println(fetchText(url + s, enc, regex, template)))
        
    }

}


