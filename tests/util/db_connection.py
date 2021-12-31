from pathlib import Path
from ethgreen.util.db_wrapper import DBWrapper
import tempfile
import aiosqlite


class DBConnection:
    async def __aenter__(self) -> DBWrapper:
        self.db_path = Path(tempfile.NamedTemporaryFile().name)
        if self.db_path.exists():
            self.db_path.unlink()
        self.connection = await aiosqlite.connect(self.db_path)
        return DBWrapper(self.connection)

    async def __aexit__(self, exc_t, exc_v, exc_tb):
        await self.connection.close()
        self.db_path.unlink()
