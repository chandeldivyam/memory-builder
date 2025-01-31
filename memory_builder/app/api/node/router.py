from fastapi import APIRouter, Depends, HTTPException
from app.schemas.node import Node
from app.api.node.service import NodeService
from typing import Optional, List

router = APIRouter(prefix="/node", tags=["node"])

@router.get("/", response_model=List[Optional[Node]])
async def get_nodes(node_service: NodeService = Depends()):
    return node_service.get_nodes()
