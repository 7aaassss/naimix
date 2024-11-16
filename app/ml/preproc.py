import re

class Processor:
    def __init__(self, filepath, keywords=None, before=2, after=2):
        with open(filepath, 'r', encoding='utf-8') as file:
            self.text = file.read()
        self.work_keywords = keywords or ["job", "working", "profession", "career"]
        self.before = before
        self.after = after

    def extract_work_related_contexts(self):
        """
        Извлекает контексты вокруг предложений, связанных с работой, с заданным количеством предложений до и после, без дубликатов.

        Returns:
            Список уникальных контекстов (списков предложений).
        """

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