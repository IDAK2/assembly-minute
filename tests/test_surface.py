from pathlib import Path
T=Path('contracts/contract.py').read_text();P=Path('docs/index.html').read_text()
def test_surface():
 for n in ('open_motion','adopt','publish','object_minute','reconcile','finalize','get_minute'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="chamber"' in P and 'id="minuteTape"' in P
