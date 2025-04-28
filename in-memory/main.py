from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import torch

documents = [
  {
    "id": 1,
    "text": "O Parque Nacional da Chapada Diamantina, localizado no coração da Bahia, é um espetáculo da natureza com seus vales profundos, cachoeiras cristalinas e formações rochosas impressionantes. A Cachoeira da Fumaça, com seus 380 metros de queda livre, é uma das principais atrações, oferecendo um visual deslumbrante especialmente durante a estação das chuvas. A região também abriga grutas misteriosas como a Gruta da Pratinha, com suas águas azul-turquesa que refletem as formações calcárias."
  },
  {
    "id": 2,
    "text": "A arte do origami japonês vai muito além de simples dobraduras de papel. Esta prática milenar, que combina precisão matemática com expressão artística, pode criar desde formas simples como tsurus (garças) até complexas esculturas modulares. O papel washi, tradicionalmente feito à mão com fibras de amoreira, é o preferido pelos mestres origamistas por sua durabilidade e flexibilidade. Cada dobra carrega significado, tornando o origami uma meditação ativa que promove concentração e paz interior."
  },
  {
    "id": 3,
    "text": "O processo de fermentação do pão sourdough é uma dança microbiana fascinante. O fermento natural, ou levain, é um ecossistema vivo de leveduras selvagens e bactérias lácteas que transformam farinha e água em um produto aromático e complexo. Durante a fermentação lenta, que pode levar até 48 horas em temperatura controlada, ocorre a produção de ácidos orgânicos que dão ao pão seu característico sabor levemente ácido e textura alveolada. Cada cultura de fermento natural possui uma assinatura microbiana única, influenciada pelo ambiente local."
  },
  {
    "id": 4,
    "text": "A aurora boreal, ou luzes do norte, é um fenômeno atmosférico que transforma o céu noturno em um espetáculo de cores dançantes. Ocorre quando partículas carregadas do vento solar colidem com átomos na magnetosfera terrestre, liberando energia em forma de fótons. As cores variam conforme o gás atingido: oxigênio produz tons verdes e vermelhos, enquanto o nitrogênio emite luzes azuis e púrpuras. Os melhores lugares para observação incluem Tromsø na Noruega, Fairbanks no Alasca e o norte da Islândia, especialmente durante os equinócios."
  },
  {
    "id": 5,
    "text": "A construção das catedrais góticas na Europa medieval representou um marco na engenharia e arquitetura. Com seus arcos ogivais, vitrais coloridos e arcobotantes, edifícios como Notre-Dame de Paris desafiaram as leis da física da época. Os vitrais, compostos por milhares de peças de vidro pintado, contavam histórias bíblicas em um jogo de luz e cor que impressionava os fiéis. A rosácea, elemento característico das fachadas, simbolizava tanto a perfeição divina quanto os avanços matemáticos do período."
  }
]

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

doc_embeddings = {doc["id"]: model.encode(doc['text'], convert_to_tensor=True) for doc in documents}

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query(request: QueryRequest):
    
    query_embedding = model.encode(request.query, convert_to_tensor=True)
    
    similarities = {
        doc_id: torch.cosine_similarity(query_embedding.unsqueeze(0), emb.unsqueeze(0)).item()
        for doc_id, emb in doc_embeddings.items()
    }

    best_doc_id = max(similarities, key=similarities.get)
    best_doc = next(doc for doc in documents if doc["id"] == best_doc_id)
    
    return {
        "query": request.query,
        "best_document": {
            "id": best_doc["id"],
            "text": best_doc["text"],
            "similarity": similarities[best_doc_id]
        }
    }