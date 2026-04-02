
paragraph_placeholder = " ... "
open_paragraph_tag = "<p>"
close_paragraph_tag = "</p>"

class Format:
    @staticmethod
    def format_text(text: str) -> str:
        formatted_text_list = text.split(paragraph_placeholder)

        formatted_text = formatted_text_list[0]

        for paragraph in formatted_text_list[1:]:
            formatted_text += open_paragraph_tag + paragraph + close_paragraph_tag

        return formatted_text