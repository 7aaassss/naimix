import re

class Processor:
    def __init__(self, text, keywords=None, before=2, after=2):
        self.text = text
        self.work_keywords = keywords or ["job", "working", "profession", "career"]
        self.before = before
        self.after = after

    def extract_work_related_contexts(self):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', self.text)
        extracted_contexts = []
        seen_contexts = set()

        for i, sentence in enumerate(sentences):
            for keyword in self.work_keywords:
                if keyword in sentence.lower():
                    start_index = max(0, i - self.before)
                    end_index = min(i + self.after + 1, len(sentences))
                    context = tuple(sentences[start_index:end_index])

                    if context not in seen_contexts:
                        seen_contexts.add(context)
                        extracted_contexts.append(context)

                    break

        return [list(context) for context in extracted_contexts]